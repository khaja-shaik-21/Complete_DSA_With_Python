class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.endOfString = True
        print(f'"{word}" inserted successfully.')

    def search(self, word):
        if not self.root.children:
            print("Trie is empty. Nothing to search.")
            return False

        current = self.root
        for ch in word:
            if ch not in current.children:
                print(f"'{word}' Word not found in Trie.")
                return False
            current = current.children[ch]
        
        if current.endOfString:
            print(f"'{word}' Word found in Trie.")
            return True
        else:
            print(f"'{word}' Word not found in Trie.")
            return False


    def delete(self, word):
        if not self.root.children:
            print("Trie is empty. Nothing to delete.")
            return

        result = self._delete(self.root, word, 0)
        if result:
            print(f'"{word}" deleted successfully.')
        else:
            print(f'"{word}" not found.')


    def _delete(self, current, word, index):
        if index == len(word):
            if not current.endOfString:
                return False  
            current.endOfString = False
            return len(current.children) == 0  

        ch = word[index]
        node = current.children.get(ch)
        if node is None:
            return False  

        should_delete_current_node = self._delete(node, word, index + 1)

        if should_delete_current_node:
            del current.children[ch]
            return len(current.children) == 0 and not current.endOfString
        return False

    def print_all_words(self):
        if not self.root.children:
            print("Trie is empty. No words to display.")
            return
        print("Word in Trie:")
        self._print_helper(self.root, "")


    def _print_helper(self, node, word):
        if node.endOfString:
            print(word)
        for ch, child_node in node.children.items():
            self._print_helper(child_node, word + ch)
    
    def delete_trie(self):
        if not self.root.children:
            print("Trie is already empty.")
        else:
            self.root = TrieNode()
            print("Trie has been deleted.")



# ----------------- Menu-Driven Program -----------------

def menu():
    trie = Trie()
    while True:
        print("\n----- TRIE OPERATIONS MENU -----")
        print("1. Insert Word")
        print("2. Search Word")
        print("3. Delete Word")
        print("4. Print All Words in Trie")
        print("5. Delete Entire Trie")  
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            word = input("Enter word to insert: ").strip()
            trie.insert(word)
        elif choice == "2":
            word = input("Enter word to search: ").strip()
            trie.search(word)
        elif choice == "3":
            word = input("Enter word to delete: ").strip()
            trie.delete(word)  
        elif choice == "4":
            trie.print_all_words()
        elif choice == "5":
            trie.delete_trie()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

menu()


#############   Time & Space Complexity Table: Trie (Prefix Tree) using HashMap (Dict)  ############

# | Operation              | Time Complexity   | Space Complexity   | Notes                                                     |
# |------------------------|-------------------|--------------------|-----------------------------------------------------------|
# | insert(word)           | O(L)              | O(AL)              | L = length of word, A = alphabet size (for new nodes)     |
# | search(word)           | O(L)              | O(1)               | Checks character by character in word                     |
# | delete(word)           | O(L)              | O(L)               | Recursively deletes nodes if unused                       |
# | startsWith(prefix)     | O(P)              | O(1)               | P = length of prefix                                      |
# | print_all_words()      | O(N * L)          | O(L)               | N = number of words, L = average word length              |
# | delete_trie()          | O(1)              | O(1)               | Resets root node                                          |
# | is_empty check         | O(1)              | O(1)               | Just checks if root has children                          |
