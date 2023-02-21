use clap::{arg, command, Parser, Subcommand, ArgGroup};

mod create;

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands
}

#[derive(Subcommand)]
enum Commands {
    Create,
    #[command(group(
        ArgGroup::new("get-set")
            .multiple(false)
            .args(["get", "set"])
    ), arg_required_else_help=true)]
    Config {
        /// Fetch a config value
        #[arg(short, long, value_names=["GROUP", "KEY"])]
        get: Vec<String>,
        /// Create or update a config value
        #[arg(short, long, value_names=["GROUP", "KEY_ASSIGN"])]
        set: Vec<String>
    },
    Start {
        #[arg(short, long)]
        force_new: bool,
        #[arg(short='n', long, value_name="SESSION")]
        from_name: String
    }
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Create => {
            create::get_input()
                .and_then(|(name, urls)| create::write_session(name, urls))
                .unwrap_or_default();
        }

        Commands::Config { get, set } => {
            if get.len() == 2 {
                println!("config --get {:?}", get);
            } else if set.len() == 2 {
                println!("config --set {:?}", set);
            }
        }

        Commands::Start { force_new, from_name } => {
            println!("start -f={} -n {}", force_new, from_name);
        }
    }
}
