use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut h: HashMap<i32, i32> = HashMap::new();
        for (i, n) in nums.iter().enumerate() {
            let complement = target - n;
            if let Some(j) = h.get(&complement) {
                return vec![i as i32, *j];
            } else {
                h.insert(*n, i as i32);
            }
        }
        unreachable!()
    }
}