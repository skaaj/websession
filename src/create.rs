use std::fs::File;
use std::io::{self, Write};
use std::fs::File;
use std::fs::create_dir_all;
use std::path::Path;
use serde_json::json;
use serde_json::to_string_pretty;

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
    let path = Path::new(".")
        .join("config")
        .join("user")
        .join(format!("{name}.json"));

    if let Some(parent_path) = path.parent() {
        if !parent_path.exists() {
            create_dir_all(parent_path)?;
        }
        let json_record = json!({
            "name": name,
            "urls": urls
        });
        File::create(path)?
            .write_all(to_string_pretty(&json_record)?.as_bytes())?;
    }

    Ok(())
}
