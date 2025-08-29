# Bookstore Agent using Parlant SDK
import parlant.sdk as p
import asyncio
from datetime import datetime

# Tools
@p.tool
async def list_available_books(context: p.ToolContext) -> p.ToolResult:
    return p.ToolResult(
        data=["1984 by George Orwell", "Atomic Habits by James Clear", "Dune by Frank Herbert",
              "The Complete Chess Course by Fred Reinfeld", "Americanah by Chimamanda Ngozi Adichie"]
    )


@p.tool
async def check_stock(context: p.ToolContext, title: str) -> p.ToolResult:
    # stock info
    stock = {
        "1984": "In stock",
        "Atomic Habits": "Only 2 copies left",
        "Dune": "Out of stock",
        "The Complete Chess Course": "In stock",
        "Americanah": "In stock",
    }
    return p.ToolResult(data=stock.get(title, "Not found"))


@p.tool
async def recommend_books(context: p.ToolContext) -> p.ToolResult:
    return p.ToolResult(data=["The Alchemist by Paulo Coelho", "Sapiens by Yuval Noah Harari",
                              "Bobby Fischer Teaches Chess by Bobby Fischer", "Half of a Yellow Sun by Chimamanda Ngozi Adichie"])


@p.tool
async def place_order(context: p.ToolContext, title: str, date: datetime) -> p.ToolResult:
    return p.ToolResult(data=f"Your order for '{title}' has been placed on {date.strftime('%Y-%m-%d')}.")


# Glossary
async def add_domain_glossary(agent: p.Agent) -> None:
    # Add domain-specific terms to the agent's glossary
    await agent.create_term(
        name="Store Phone Number",
        description="The phone number of our bookstore is +1-222-333-4444",
    )

    await agent.create_term(
        name="Store Hours",
        description="Store hours are Monday to Saturday, 9 AM to 8 PM",
    )

    await agent.create_term(
        name="Store Location",
        description="We are located at 123 Main Street, Springfield.",
    )


# Journeys
# Purchase Journey
async def create_purchase_journey(server: p.Server, agent: p.Agent) -> p.Journey:
    journey = await agent.create_journey(
        title="Book Purchase",
        description="Helps a customer find and buy a book.",
        conditions=["The customer wants to buy a book"],
    )

    # Define the states and transitions
    t0 = await journey.initial_state.transition_to(tool_state=list_available_books)

    t1 = await t0.target.transition_to(
        chat_state="List available books and ask which one they want"
    )

    t2 = await t1.target.transition_to(
        tool_state=check_stock,
        condition="The customer selects a book",
    )

    t3 = await t2.target.transition_to(
        chat_state="Tell the customer the stock status",
    )

    t4 = await t3.target.transition_to(
        tool_state=place_order,
        condition="The book is in stock and the customer wants to place an order",
    )

    # Final confirmation state
    await t4.target.transition_to(
        chat_state="Confirm the order has been placed",
    )

    # Handle out of stock scenario
    await t3.target.transition_to(
        tool_state=recommend_books,
        condition="The book is out of stock and the customer wants alternatives",
    )

    return journey


# Main
async def main() -> None:
    # Initialize the server and agent
    async with p.Server() as server:
        agent = await server.create_agent(
            name="Bookstore Agent",
            description="Friendly and helpful, assists customers with books and orders.",
        )

        # Add glossary terms
        await add_domain_glossary(agent)
        purchase_journey = await create_purchase_journey(server, agent)

        # Example observation
        await agent.create_observation(
            "The customer is asking about a book but it's not clear whether they want to buy or get recommendations",
        )

        # Create guidelines
        await agent.create_guideline(
            condition="The customer asks about store hours",
            action="Tell them our store hours",
        )

        await agent.create_guideline(
            condition="The customer asks about location",
            action="Tell them our store address",
        )

        await agent.create_guideline(
            condition="The customer asks to speak to a staff member",
            action="Ask them to call the store phone number",
        )

        await agent.create_guideline(
            condition="The request has nothing to do with books",
            action="Politely explain that you can only help with bookstore-related questions.",
        )

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
