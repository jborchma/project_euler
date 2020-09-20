// Solution to problem 3 in Rust

fn main() {
    let mut limit: u64 = 600851475143;
    let mut i: u64 = 2;
    // we only need to search until sqrt(limit)
    while i * i < limit {
        // if we find a divisor, divide it out as much as possible
        while limit % i == 0 {
            limit = limit / i;
        }
        i += 1
    }
    println!("The answer is {}", limit)
}
