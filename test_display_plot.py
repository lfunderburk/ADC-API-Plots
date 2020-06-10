from IPython.display import HTML
import glob, os

        
    
if __name__ == "__main__":
    
    os.chdir("./ADC-API-Plots/")
    for file in glob.glob("*.html"):
        display(HTML(filename=file))
