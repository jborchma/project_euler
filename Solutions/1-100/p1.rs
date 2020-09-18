// Solution to problem 1 in rust

fn main() {
    // create a mutable counter with annotation
    let mut summe: u32 = 0;
    // loop through numbers up until but excluding 1000
    for n in 1..1000 {
        if n % 3 == 0 {
            summe += n;
        }
        else if n % 5 == 0 {
            summe += n;
        }
    }
    println!("{}", summe)

}
