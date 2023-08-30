import heapq
 2 
 
from collections import defaultdict
 3 
 
 4 
 
class HuffmanNode:
 5 
 
    def __init__(self, character=None, frequency=None):
 6 
 
        self.character = character
 7 
 
        self.frequency = frequency
 8 
 
        self.left = None
 9 
 
        self.right = None
 10 
 
    
 11 
 
    def __lt__(self, other):
 12 
 
        return self.frequency < other.frequency
 13 
 
 14 
 
def build_frequency_table(text):
 15 
 
    frequency_table = defaultdict(int)
 16 
 
    for char in text:
 17 
 
        frequency_table[char] += 1
 18 
 
    return frequency_table
 19 
 
 20 
 
def build_huffman_tree(frequency_table):
 21 
 
    heap = []
 22 
 
    for char, frequency in frequency_table.items():
 23 
 
        node = HuffmanNode(char, frequency)
 24 
 
        heapq.heappush(heap, node)
 25 
 
    while len(heap) > 1:
 26 
 
        left_child = heapq.heappop(heap)
 27 
 
        right_child = heapq.heappop(heap)
 28 
 
        parent = HuffmanNode(frequency=left_child.frequency + right_child.frequency)
 29 
 
        parent.left = left_child
 30 
 
        parent.right = right_child
 31 
 
        heapq.heappush(heap, parent)
 32 
 
    return heap[0]
 33 
 
 34 
 
def build_huffman_codes(huffman_tree):
 35 
 
    codes = {}
 36 
 
    
 37 
 
    def build_codes_helper(node, current_code):
 38 
 
        if node is None:
 39 
 
            return
 40 
 
        if node.character:
 41 
 
            codes[node.character] = current_code
 42 
 
            return
 43 
 
        build_codes_helper(node.left, current_code + "0")
 44 
 
        build_codes_helper(node.right, current_code + "1")
 45 
 
    
 46 
 
    build_codes_helper(huffman_tree, "")
 47 
 
    return codes
 48 
 
 49 
 
def encode_text(text, codes):
 50 
 
    encoded_text = ""
 51 
 
    for char in text:
 52 
 
        encoded_text += codes[char]
 53 
 
    return encoded_text
 54 
 
 55 
 
def decode_text(encoded_text, huffman_tree):
 56 
 
    decoded_text = ""
 57 
 
    current_node = huffman_tree
 58 
 
    for bit in encoded_text:
 59 
 
        if bit == "0":
 60 
 
            current_node = current_node.left
 61 
 
        else:
 62 
 
            current_node = current_node.right
 63 
 
        if current_node.character:
 64 
 
            decoded_text += current_node.character
 65 
 
            current_node = huffman_tree
 66 
 
    return decoded_text
 67 
 
 68 
 
def main():
 69 
 
    # Example usage
 70 
 
    text = "hello world"
 71 
 
    print("Original Text:", text)
 72 
 
    
 73 
 
    frequency_table = build_frequency_table(text)
 74 
 
    huffman_tree = build_huffman_tree(frequency_table)
 75 
 
    codes = build_huffman_codes(huffman_tree)
 76 
 
    encoded_text = encode_text(text, codes)
 77 
 
    print("Encoded Text:", encoded_text)
 78 
 
    
 79 
 
    decoded_text = decode_text(encoded_text, huffman_tree)
 80 
 
    print("Decoded Text:", decoded_text)
 81 
 
 82 
 
if __name__ == "__main__":
 83 
 
    main()
 84 
 
