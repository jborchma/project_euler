// Solution to problem 2 in rust

fn main() {
    // create a vector for the Fibonnacci elements (mutable, of course)
    let mut fibon_elements: Vec<u64> = vec![1; 2];
    // create mutable tracker for the while loop
    let mut small = true;
    // needs to be u64 so that we can compare it to the elements in the vector
    let limit: u64 = 4000000;
    while small {
        // sum the last two elements
        let len = fibon_elements.len();
        let new_element = fibon_elements[len - 1] + fibon_elements[len - 2];
        // add the new element to the vector
        fibon_elements.push(new_element);
        // if we are above our limit, abort loop by changing small
        if new_element > limit {
            small = false
        }
    }
    // only keep even element by using summation from iterator
    // need to assign type to the sum
    fibon_elements.retain(|&i|i % 2 == 0);
    let summe: u64 = fibon_elements.iter().sum();
    println!("The answer is: {}", summe)
}
