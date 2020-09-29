// Solution to problem 4 in request

fn is_palindrome(number: u64) -> bool {
    let mut reversed = 0;
    let mut copy = number;
    while copy > 0 {
        reversed *= 10;
        // add last digit
        reversed += copy % 10;
        // since copy is an integer, throws away anything after the ,
        copy /= 10;
    }
    number == reversed
}

fn main() {
    let mut largest: u64 = 0;
    //initialize temp variable without initial value
    let mut temp_product: u64;
    for first in 100..1000 {
        for second in 100..1000 {
            temp_product = first * second;
            if is_palindrome(temp_product) & (temp_product > largest) {
                largest = temp_product
            }
        }
    }
    println!("The answer is: {}", largest)
}
