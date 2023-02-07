use clap::{arg, command, Parser, Subcommand, ArgGroup};

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
        from_name: Option<String>,
        #[arg(short='b', long, value_names=["PROFILE_PATH", "BOOKMARKS_PATH"])]
        from_bookmarks: Option<String>
    }
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Create => {
            println!("create");
        }

        Commands::Config { get, set } => {
            println!("config {:?} {:?}", get, set);
        }

        Commands::Start { force_new, from_name, from_bookmarks } => {
            println!("start {:?} {:?} {:?}", force_new, from_name, from_bookmarks);
        }
    }
}
