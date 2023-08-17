from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import pandas as pd

ukBrStanovnika = 11760

shapefile_path = r'C:\Users\Nina\Desktop\GIS Programiranje\Batocina Naselja.shp'
naselja= gpd.read_file(shapefile_path)

naselja.crs
print(naselja.crs)
naselja.crs = from_epsg(6316)
naselja.crs
print(naselja.crs)

naselja.plot(color='lightgray', edgecolor='black')
plt.title("Batocina Naselja")
##plt.show()

df = pd.read_excel('C:\\Users\\Nina\\Desktop\\GIS Programiranje\\Book1.xlsx')
#rodjeni = df['RODJENI']
#umrli = df['UMRLI']
prirodniPrirastaj = []
df['PRIRODNI PRIRASTAJ'] = df['RODJENI'] - df['UMRLI']
df['STOPA NATALITETA'] = (df['RODJENI'] / ukBrStanovnika) * 1000
df['STOPA MORTALITETA'] = (df['UMRLI'] / ukBrStanovnika) * 1000



print(df)
#excel_file = r'C:\Users\Nina\Desktop\GIS Programiranje\Book1.xlsx'
#df = pd.read_excel(excel_file)


#1. Loading data from an excel file
#excel_file = "data_info.xlsx"
#dtf = pd.read_excel(r"data_info.xlsx",sheet_name='ASTMA')
#dtf = pd.read_excel(r"data_info.xlsx")
#print(dtf.head())



