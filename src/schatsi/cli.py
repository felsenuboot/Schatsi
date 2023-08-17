import click
import nltk


from schatsi.jobs import *

@click.command()
@click.option('-i', '--input_path', help='The path where all files to process can be found.')
@click.option('-o', '--output_path', help='The path where results are put')
@click.option('-f', '--functional_terms', help='Path to a CSV with all funtional termns')
@click.option('-n', '--negative_terms', help='Path to a CSV with all negative termns')
@click.option('-p', '--parallel', default=True, help='Prallel processing or not')
@click.option('-m', '--menu', 'menu', help="Show a guided menu to select the options", flag_value=True)
def cli(input_path, output_path, functional_terms, negative_terms, parallel, menu):
    if menu:
        print("This is where the menu will be")
    else:
        pass
    if input_path:
        nltk.download("punkt")
        if parallel:
            job = ParallelJob(input_path, output_path, functional_terms, negative_terms)
        else:
            job = SingleJob(input_path, output_path, functional_terms, negative_terms)
        job.process()
    else:
        print("You have not provided an input path. Please use the -i option to provide one.")

if __name__ == "__main__":
    job = ParallelJob("data/input", "data/output", "data/metadata/functional_terms.csv", "data/metadta/negative_terms.csv")
    job.process()
    
    