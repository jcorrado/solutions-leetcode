(ns implement-trie)

;; https://leetcode.com/problems/implement-trie-prefix-tree

(defn create-trie [] {})

(defn insert [trie word]
  (assoc-in trie (seq word) true))

(defn search [trie word]
  (true? (get-in trie (seq word))))

(defn starts-with [trie prefix]
  (map? (get-in trie (seq prefix))))

(comment

  ;; Explanation
  ;; Trie trie = new Trie();
  ;; trie.insert("apple");
  ;; trie.search("apple");   // return True
  ;; trie.search("app");     // return False
  ;; trie.startsWith("app"); // return True
  ;; trie.insert("app");
  ;; trie.search("app");     // return True

  (def t (-> (create-trie)
             (insert "apple")))

  (search t "apple")
  ;; true

  (search t "app")
  ;; false

  (starts-with t "app")
  ;; true
  
  (def t (-> (create-trie)
             (insert "apple")
             (insert "app")))

  (search t "app")
  ;; true

  ;; But we've clobbered "apple"!  This is not a Trie
  t
  ;; {\a {\p {\p true}}}
  )
