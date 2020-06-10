from IPython.display import HTML
import glob, os

        
    
if __name__ == "__main__":
    
    for file in glob.glob("./ADC-API-Plots/*.html"):
        display(HTML(filename=file))
