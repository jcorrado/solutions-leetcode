(ns implement-trie)

;; https://leetcode.com/problems/implement-trie-prefix-tree

(defn create-trie [] {})

(defn insert [trie word]
  (assoc-in trie (conj (vec word) nil) true))

(defn search [trie word]
  (true? (get-in trie (conj (vec word) nil))))

(defn starts-with [trie prefix]
  (boolean
   (some some? (keys (get-in trie prefix)))))

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

  ;; Confirm we haven't clobbered "apple"!
  (search t "apple")
  ;; true

  t
  ;; {\a {\p {\p {\l {\e {nil true}},
  ;;              nil true}}}}
  )
