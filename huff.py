import heapq

# Define a Node class to represent nodes in the Huffman tree
class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# Build the Huffman tree
def build_tree(text):
    frequency = {}
    # Calculate frequency of each character in the text
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Create a priority queue to store nodes
    pq = [Node(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(pq)

    # Build the Huffman tree
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)

    return pq[0]

# Build the Huffman codes table
def build_codes(root):
    codes = {}

def traverse(node, code=""):
    if node.symbol is not None:
        codes[node.symbol] = code
        return
    traverse(node.left, code + "0")
    traverse(node.right, code + "1")

    traverse(root)
    return codes

# Compress the text using Huffman coding
def compress(text):
    root = build_tree(text)
    codes = build_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return root, encoded_text

# Decompress the text using Huffman coding
def decompress(root, bitflow):
    node = root
    decoded_text = ""

    for bit in bitflow:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.symbol is not None:
            decoded_text += node.symbol
            node = root

    return decoded_text

# Utility function to read content of a file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Utility function to write content to a file
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Compress a file using Huffman coding
def compress_file(input_filename, output_filename):
    text = read_file(input_filename)
    root, bitflow = compress(text)
    write_file(output_filename, bitflow)

# Decompress a file using Huffman coding
def decompress_file(input_filename, output_filename):
    bitflow = read_file(input_filename)
    root = None  # Root node is not saved in the compressed file
    decoded_text = decompress(root, bitflow)
    write_file(output_filename, decoded_text)

# Example usage:
if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "compressed.hfz"
    compress_file(input_filename, output_filename)
    decompress_file(output_filename, "decompressed.txt")