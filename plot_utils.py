import matplotlib as mpl


def set_presentation_params():
    """Set the matplotlib rcParams to values for presentation-size figures.
    
    """
    mpl.rcParams["axes.titlesize"] = 90
    mpl.rcParams["axes.labelsize"] = 80
    mpl.rcParams["xtick.labelsize"] = 60
    mpl.rcParams["ytick.labelsize"] = 60
    mpl.rcParams["legend.fontsize"] = 60
    mpl.rcParams["figure.figsize"] = (25, 25)
    mpl.rcParams["image.cmap"] = "gray"
    mpl.rcParams["lines.markersize"] = 14
    mpl.rcParams["lines.linewidth"] = 15
    mpl.rcParams["font.size"] = 60
    mpl.rcParams["xtick.major.size"] = 10
    mpl.rcParams["xtick.major.width"] = 3
    mpl.rcParams["ytick.major.size"] = 10
    mpl.rcParams["ytick.major.width"] = 3
    
    
def set_print_params():
    """Set the matplotlib rcParams to values for print-size figures.
    
    """
    mpl.rcParams["axes.titlesize"] = 25
    mpl.rcParams["axes.labelsize"] = 20
    mpl.rcParams["xtick.labelsize"] = 15
    mpl.rcParams["ytick.labelsize"] = 15
    mpl.rcParams["legend.fontsize"] = 15
    mpl.rcParams["figure.figsize"] = (8, 8)
    mpl.rcParams["image.cmap"] = "gray"
    mpl.rcParams["lines.markersize"] = 5
    mpl.rcParams["lines.linewidth"] = 3
    mpl.rcParams["font.size"] = 15

