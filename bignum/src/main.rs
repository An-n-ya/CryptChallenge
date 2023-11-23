use num_bigint::BigUint;
use num_traits::One;

fn mersenne(exp: u32) -> BigUint {
    let base: BigUint = BigUint::from(2u32);
    let one: BigUint = One::one();
    base.pow(exp) - one
}

fn factorial_prime(n: usize) -> BigUint {
    let mut res: BigUint = One::one();
    for i in 1..n {
        res = i * &res;
        // This is a low cost way of swapping f0 with f1 and f1 with f2.
    }
    res - BigUint::from(1u32)
}

fn main() {
    let n = 82589933;
    let nn = 6917;
    println!("mersenne({}) = {}", nn, factorial_prime(nn));
}
