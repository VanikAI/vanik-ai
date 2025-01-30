import click
from .blockchain.interactor import BlockchainManager
from .llm.emotion_engine import EmotionAnalyzer

@click.group()
def cli():
    """VANIK Command Line Interface"""
    
@cli.command()
@click.option('--network', default='testnet')
def start(network):
    """Start interactive mode"""
    click.echo(f"🚀 Starting VANIK on {network} network...")
    # Initialize components
    BlockchainManager(network=network)
    EmotionAnalyzer()
    click.echo("✅ Systems ready!")

if __name__ == "__main__":
    cli()
