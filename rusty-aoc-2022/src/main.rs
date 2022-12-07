use std::env;
// use std::fmt::format;
use std::fs;
// use error_chain::error_chain;
// use std::io::Read;
use std::collections::HashMap;

// error_chain! {
//     foreign_links {
//         Io(std::io::Error);
//         HttpRequest(reqwest::Error);
//     }
// }

// #[tokio::main]
fn main() {
    let args: Vec<String> = env::args().collect();
    let problem_num = &args[1];

    println!("Problem number {}", problem_num);

    // let input_file_body = fetch_file().await;
    // println!("body = {:#?}", input_file_body);
    let mut scores = HashMap::new();
    scores.insert(String::from("A X"), 3);
    scores.insert(String::from("A Y"), 4);
    scores.insert(String::from("A Z"), 8);
    scores.insert(String::from("B X"), 1);
    scores.insert(String::from("B Y"), 5);
    scores.insert(String::from("B Z"), 9);
    scores.insert(String::from("C X"), 2);
    scores.insert(String::from("C Y"), 6);
    scores.insert(String::from("C Z"), 7);

    let file_path:String = format!("./inputs/input_{problem_num}.txt");
    println!("input path: {}", file_path);
    let contents:String = fs::read_to_string(file_path).expect("Couldn't read file.");

    let values = contents.split("\n");

    // let mut new_values: Vec<i32> = vec![];    

    // let team_name = String::from("Blue");
    // let score = scores.get(&team_name).copied().unwrap_or(0);

    // for (key, value) in &scores {
    //     println!("{}: {}", key, value);
    // }
    let mut res: i32 = 0;

    for v in values {
        let g = String::from(v);
        res = res + scores.get(&g).copied().unwrap_or(0);
    
        // let mynums: Vec<i32> = nums.split("\n").map(|x| x.parse::<i32>().unwrap()).collect();
        // let sum: i32 = mynums.iter().sum();
        // new_values.push(sum);
            // let sum: u8 = num.iter().sum();
            // let my_int: i32 = num.parse().unwrap();
            // new_values.push(sum);
        } 

    // new_values.sort();
    // new_values.reverse();
    
    println!("reslut: {}", res);
    // println!("summed: {:?}", new_values[0] + new_values[1] + new_values[2]);

    // println!("With text:\n{values}");
}

// fn read_file(file_path:String) ->  Result<String, Box<dyn std::error::Error>> {
//     let contents:String = fs::read_to_string(file_path).expect("Couldn't read file.");
//     Ok(contents)
// }

// async fn fetch_file() -> Result<String, Box<dyn std::error::Error>> {

//     let problem_num = "1";
//     let client = reqwest::Client::new();
//     let res = client.get(format!("https://adventofcode.com/2022/day/{problem_num}")).send().await?;
//     // let mut res = reqwest::blocking::get("https://adventofcode.com/2022/day/" + problem_num).await?;
//     // let mut body = String::new();
//     // res.read_to_string(&mut body)?;
//     let body = res.text().await?;
    
//     // println!("Status: {}", res.status());
//     // println!("Headers:\n{:#?}", res.headers());
//     // println!("Body:\n{}", body);

//     Ok(body)

// }