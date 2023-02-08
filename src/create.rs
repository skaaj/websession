use std::io::{self, Write};
use serde_json::json;

pub fn get_input() -> io::Result<(String, Vec<String>)> {
    let mut session_name = String::new();
    let mut urls = Vec::new();

    print!("Session name: ");
    io::stdout().flush()?;
    io::stdin().read_line(&mut session_name)?;

    loop {
        let mut url_input = String::new();
        print!("URL {} (q to quit): ", urls.len() + 1);
        io::stdout().flush()?;
        io::stdin().read_line(&mut url_input)?;
        match url_input.trim() {
            "q" => break,
            value => urls.push(value.to_string()),
        }
    }

    Ok((session_name.trim().to_string(), urls))
}

pub fn write_session(name: String, urls: Vec<String>) -> io::Result<()> {
    let json_record = json!({
        "name": name,
        "urls": urls
    });

    println!("{}", json_record.to_string());

    Ok(())
}
