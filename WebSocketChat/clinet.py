import asyncio
import websockets

async def send_message():
    uri = "ws://192.168.167.114"  # WebSocket server address
    async with websockets.connect(uri) as websocket:
        while True:
            # Read input from the user
            message = input("Enter message (or 'exit' to quit): ")
            
            # Check if user wants to exit
            if message.lower() == 'exit':
                break
            
            # Send the message to the server
            await websocket.send(message)
            print(f"Sent message to server: {message}")
            
            # Wait for the response from the server
            response = await websocket.recv()
            print(f"Received response from server: {response}")

# Run the client
asyncio.run(send_message())
