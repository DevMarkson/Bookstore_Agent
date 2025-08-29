# Bookstore Agent

A conversational AI agent built with Parlant SDK that helps customers browse books, check inventory, and place orders at Cozy Corner Bookstore.

## Overview

This bookstore agent is designed to provide friendly and helpful interactions with customers while assisting them with:

- **Book Discovery**: Browse available books and find specific titles
- **Stock Information**: Check availability and stock levels of books
- **Order Placement**: Help customers purchase books they want
- **Recommendations**: Suggest books based on customer interests
- **Store Information**: Provide store hours, location, and contact details

The agent is built using conversational journeys that guide customers through the book purchasing process, ensuring they find what they're looking for while maintaining a welcoming bookstore atmosphere.

## Features

### 📚 Book Purchase Journey

- Lists available books in the store inventory
- Checks stock status for specific titles
- Handles order placement for in-stock books
- Provides alternative recommendations for out-of-stock items
- Confirms successful order placement

### 🔍 Smart Book Discovery

- **Available Books**: Fiction, non-fiction, chess books, and international literature
- **Stock Checking**: Real-time inventory status
- **Recommendations**: Curated book suggestions when requested
- **Special Collections**: Chess books and works by acclaimed authors like Chimamanda Ngozi Adichie

### 🏪 Store Information

- **Store Hours**: Monday to Saturday, 9 AM to 8 PM
- **Location**: 123 Main Street, Springfield
- **Contact**: +1-222-333-4444
- **Staff Assistance**: Direct customers to call for human support

### 📖 Book Inventory

**Current Available Books:**

- 1984 by George Orwell
- Atomic Habits by James Clear
- Dune by Frank Herbert
- The Complete Chess Course by Fred Reinfeld
- Americanah by Chimamanda Ngozi Adichie

**Recommendation Collection:**

- The Alchemist by Paulo Coelho
- Sapiens by Yuval Noah Harari
- Bobby Fischer Teaches Chess by Bobby Fischer
- Half of a Yellow Sun by Chimamanda Ngozi Adichie

## Installation

### Prerequisites

- Python 3.8 or higher
- An OpenAI API key

### Step 1: Install Parlant SDK

```bash
pip install parlant
```

### Step 2: Set Up Environment Variables

**For Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY = "your-openai-api-key-here"
```

**For Windows Command Prompt:**

```cmd
set OPENAI_API_KEY=your-openai-api-key-here
```

**For Linux/macOS:**

```bash
export OPENAI_API_KEY=your-openai-api-key-here
```

### Step 3: Clone or Download the Agent

Save the `bookstore.py` file to your desired directory.

### Step 4: Run the Agent

```bash
python bookstore.py
```

## Usage

Once the agent is running, customers can interact with it through natural language. The agent will:

1. **Understand Intent**: Automatically determine whether the customer wants to browse, buy, or get recommendations
2. **Guide Through Purchase**: Use conversational journeys to walk customers through book selection and ordering
3. **Provide Information**: Answer questions about store hours, location, and book availability
4. **Offer Alternatives**: Suggest similar books when requested items are out of stock

### Example Interactions

**Browsing Books:**

```
Customer: "What books do you have available?"
Agent: "We have a wonderful selection! Here are our available books: 1984 by George Orwell, Atomic Habits by James Clear, Dune by Frank Herbert, The Complete Chess Course by Fred Reinfeld, and Americanah by Chimamanda Ngozi Adichie. Which one interests you?"
```

**Checking Stock:**

```
Customer: "Do you have 1984 in stock?"
Agent: "Yes! 1984 by George Orwell is in stock. Would you like to place an order for it?"
```

**Placing an Order:**

```
Customer: "I want to buy Americanah"
Agent: "Great choice! Americanah by Chimamanda Ngozi Adichie is in stock. Your order for 'Americanah' has been placed. We'll have it ready for you!"
```

**Getting Recommendations:**

```
Customer: "Dune is out of stock, what else do you have?"
Agent: "I'm sorry Dune is currently out of stock. Let me recommend some other great books: The Alchemist by Paulo Coelho, Sapiens by Yuval Noah Harari, Bobby Fischer Teaches Chess, or Half of a Yellow Sun by Chimamanda Ngozi Adichie. Any of these sound interesting?"
```

**Store Information:**

```
Customer: "What are your store hours?"
Agent: "Our store hours are Monday to Saturday, 9 AM to 8 PM. We're closed on Sundays. Is there anything else I can help you with?"
```

## Configuration

### Customizing Book Inventory

Update the book lists in the tools:

**Available Books** (`list_available_books` function):

```python
data=["Your Book Title", "Another Book by Author", ...]
```

**Stock Status** (`check_stock` function):

```python
stock = {
    "Your Book Title": "In stock",
    "Another Book": "Only 2 copies left",
    "Third Book": "Out of stock",
}
```

**Recommendations** (`recommend_books` function):

```python
data=["Recommended Book 1", "Recommended Book 2", ...]
```

### Updating Store Information

Modify the `add_domain_glossary()` function to update:

- Store phone number
- Store hours
- Store location/address

### Adding New Tools

Create new tools by decorating functions with `@p.tool`:

```python
@p.tool
async def your_new_tool(context: p.ToolContext) -> p.ToolResult:
    # Your implementation here
    return p.ToolResult(data="Your response")
```

## Architecture

The agent is built using Parlant's key concepts:

- **Tools**: Functions that perform specific actions (e.g., listing books, checking stock, placing orders)
- **Journeys**: Structured conversation flows that guide customers through the book purchasing process
- **Guidelines**: Rules that handle specific conditions and customer requests
- **Terms**: Store-specific information and vocabulary
- **Observations**: Mechanisms to understand customer intent when it's unclear

## Safety and Best Practices

This agent is designed with customer service excellence in mind:

- ✅ **Accurate Information**: Always provides current stock status and store information
- ✅ **Helpful Alternatives**: Offers recommendations when requested items aren't available
- ✅ **Clear Boundaries**: Politely redirects non-bookstore questions to appropriate topics
- ✅ **Human Escalation**: Directs complex requests to store staff via phone

## Development

### Project Structure

```
Bookstore Agent/
├── bookstore.py          # Main agent implementation
├── parlant-data/         # Parlant SDK data directory
│   ├── cache_embeddings.json
│   ├── evaluation_cache.json
│   └── parlant.log
└── README.md            # This file
```

### Extending the Agent

To add new functionality:

1. **Create New Tools**: Add functions decorated with `@p.tool` for new capabilities
2. **Expand Journey**: Modify the purchase journey for more complex flows
3. **Add Guidelines**: Handle new types of customer requests
4. **Update Inventory**: Add new books and categories to the collection

## Testing Prompts

Use these prompts to test all agent capabilities:

### Book Discovery

- "What books do you have available?"
- "Do you have any chess books?"
- "Do you carry books by Nigerian authors?"

### Stock & Orders

- "Is 1984 in stock?"
- "I want to buy Americanah"
- "Can I order The Complete Chess Course?"

### Recommendations

- "What would you recommend?"
- "Dune is out of stock, what else do you have?"

### Store Info

- "What are your store hours?"
- "Where are you located?"
- "Can I speak to someone?"

### Edge Cases

- "Do you sell electronics?" (off-topic)
- "I need help with a book" (unclear intent)

## Troubleshooting

### Common Issues

**"export command not recognized"**

- Use PowerShell syntax: `$env:OPENAI_API_KEY = "your-key"`
- Or use Command Prompt: `set OPENAI_API_KEY=your-key`

**Import errors**

- Ensure Parlant SDK is installed: `pip install parlant`
- Check Python version compatibility (3.8+)

**API key issues**

- Verify your OpenAI API key is valid
- Ensure the environment variable is set correctly
- Check that you have sufficient API credits

### Performance

**Slow initialization**

- The agent caches entity embeddings on first run
- Subsequent runs should be much faster
- Large inventories may take longer to cache

### Logs

Check the `parlant-data/parlant.log` file for detailed execution logs and debugging information.

## Contributing

To contribute to this bookstore agent:

1. Test any changes thoroughly with various customer scenarios
2. Ensure new books are properly added to all relevant functions
3. Maintain the friendly and helpful tone in all interactions
4. Update documentation for any new functionality

## License

This project is provided as-is for educational and development purposes. Please ensure compliance with any applicable regulations before deploying in production environments.

## Support

For questions about the Parlant SDK, visit the [Parlant documentation](https://docs.parlant.ai/).

For questions about this specific bookstore agent implementation, please refer to the code comments and this README.
