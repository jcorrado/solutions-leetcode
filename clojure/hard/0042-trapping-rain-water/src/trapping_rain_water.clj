(ns trapping-rain-water)

;; https://leetcode.com/problems/trapping-rain-water/

;; from
;; [0 1 0 2 1 0 1 3 2 1 2 1]
;;
;; to:
;; [0 0 0 0 0 0 0 1 0 0 0 0]
;; [0 0 0 1 0 0 0 1 1 0 1 0]
;; [0 1 0 1 1 0 1 1 1 1 1 1]

(defn height->matrix [height]
  (loop [accum [] height height]
    (if (some pos? height)
      (recur (conj accum (map (fn [col] (if (> col 0) 1 0))
                              height))
             (map dec height))
      accum)))

(defn trim-outer-zeros [v]
  (->> v
       (drop-while zero?)
       (reverse)
       (drop-while zero?)
       (reverse)))

(defn trap [height]
  (->> (height->matrix height)
       (mapcat #(trim-outer-zeros %))
       (filter zero?)
       (count)))

(comment
  (trap [0 1 0 2 1 0 1 3 2 1 2 1])
  ;; 6

  (trap [4 2 0 3 2 5])
  ;; 9
  )
