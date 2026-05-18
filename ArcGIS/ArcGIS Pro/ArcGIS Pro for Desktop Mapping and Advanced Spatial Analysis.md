# **ArcGIS Pro for Desktop Mapping and Advanced Spatial Analysis**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*  

*Last updated: 2026*

This tutorial introduces how to import data, visualize geographic information, perform spatial analysis, and export professional maps using ArcGIS Pro.

**[Before we start](#before-we-start)**

- [Introduction	](#introduction)

- [About the tool	](#about-the-tool)

- [Datasets	](#datasets)

- [What is “spatial analysis” and “geoprocessing”?	](#what-is-spatial-analysis-and-geoprocessing)

**[Get Started](#get-started)**

- [Download and install ArcGIS Pro	](#download-and-install-arcgis-pro)

- [Create a folder	](#create-a-folder)

- [Sign in to ArcGIS Pro](#sign-in-to-arcgis-pro)

- [Create a map project](#create-a-map-project)

- [Change basemap](#change-basemap)

**[Import and Visualize Data ](#import-and-visualize-data )**

- [Shapefile	](#shapefile)

- [Table 	](#table)

- [Living Atlas ](#living-atlas )

- [Other data types 	](#other-data-types )

**[Geoprocessing](#geoprocessing)**

- [Join population and city data 	](#join-population-and-city-data )

- [Buffer ](#buffer)

- [Intersect Tool  ](#intersect-tool)

- [Calculate Coverage per District](#calculate-coverage-per-district)

- [Join coverage with citybase data](#join-coverage-with-citybase-data )

**[Save the project ](#save-the-project)**

**[Export map ](#export-map )**

- [New Layout ](#new-layout)

- [Map Title ](#map-title)

- [North Arrow and Legend ](#north-arrow-and-legend)

- [Additional Text](#additional-text)

- [Grid ](#grid)

- [Export to PDF](#export-to-pdf)

**[Export data ](#export-data)**

- [Geodatabase ](#geodatabase)

- [Table](#table)

- [Shapefile](#shapefile)

**[Resources](#resources )**

# 

# Before we start

## Introduction

In this tutorial, we will use Suzhou City’s bus stop dataset and city boundary dataset to identify underserved areas. Imagine you work for the Suzhou Department of Transport, and citizens have reported that some residential areas, particularly those near city boundaries, lack access to a bus stop within a 10‑minute walk. Your goal is to determine which city jurisdictions have the largest “service gaps” and recommend optimal locations for new stops.

Tasks covered in this tutorial include:

1. Importing datasets 
2. Performing spatial analysis (Join, Buffer, Intersect) and calculations 
3. Visualizing data on a map 
4. Exporting the map and data

By the end of this tutorial, you will be able to use ArcGIS Pro to create a district‑level map of Suzhou that shows the geographic distribution of areas without bus stop coverage.

## About the tool

ArcGIS Pro will be used in the tutorial. Visit and follow the [Downloading, Installing and Licensing ArcGIS Pro](</ArcGIS/ArcGIS Pro/Downloading, Installing and Licensing ArcGIS Pro.md>) to download and install the software on your computer. Note that ArcGIS Pro only runs on **Windows** devices.

## Datasets

[The sample dataset](</ArcGIS/ArcGIS Pro/Dataset/ArcGIS Pro Tutorial Sample Dataset.zip>) is sourced from China Geo-Explore and Figshare, and the data has been cleaned and edited for the purpose of demonstration. The folder contains three files:

- [suzhou_boundary](https://login.proxy.lib.duke.edu/login?url=http://chinageoexplorer.com/)
- [suzhou_population.csv](https://login.proxy.lib.duke.edu/login?url=http://chinageoexplorer.com/) 
- [suzhou_bus_stops.csv](https://pmc.ncbi.nlm.nih.gov/articles/PMC12886901/)

## What is “spatial analysis” and “geoprocessing”?

This tutorial introduces how to use geoprocessing tools to perform spatial analysis in ArcGIS Pro. To help ground these concepts, here is a brief overview:

**Spatial analysis**  is the process of examining geographic data based on location, relationships, and patterns. It helps answer questions such as where features are located, how they are distributed, and how they interact with other geographic elements. 

**Geoprocessing** refers to the set of operations used to manipulate, analyze, and manage geographic data. These operations include overlaying layers, buffering, clipping, dissolving, intersecting, and converting data formats. In GIS, geoprocessing tools help model spatial relationships, create new datasets from existing ones, and automate complex workflows. 

# Get Started

## Download and install ArcGIS Pro

If you haven’t downloaded ArcGIS Pro on your computer, follow the instructions in [Downloading, Installing and Licensing ArcGIS Pro](</ArcGIS/ArcGIS Pro/Downloading, Installing and Licensing ArcGIS Pro.md>) to complete.

## Create a folder

1. Download [the sample dataset](</ArcGIS/ArcGIS Pro/Dataset/ArcGIS Pro Tutorial Sample Dataset.zip>) to your computer. 
2. Create a folder on your computer to store all the files you will use and create during this tutorial. Name it as you prefer (for example, **ArcGIS Pro Tutorial**).


3. Move the sample datasets to this folder. 
4. In the folder, right-click one ZIP file and select **Extract All…** to unzip it. Repeat the same steps for the other file.


5. Open **suzhou_boundary** folder and make sure the file contents match those shown in the image below. Note that when importing a shapefile into the project, the accompanying files in the folder are **required** to support it. Without them, the shapefile may not open properly.


6. After extracting, delete the ZIP file from the folder.

## Sign in to ArcGIC Pro

1. Open ArcGIS Pro on your computer. 
2. In the pop up, select **Your ArcGIS organization’s URL**, enter **dukeuniv**, then click **Continue**.


3. Click the **Duke University** button.


4. Sign in with your NetID. If you are using your personal computer, you may check **Sign in automatically** in the bottom-left corner.


5. Once signed in, you will be directed to the ArcGIS Pro **Home** page.

## Create a map project

1. In the **Home** page, click on **Map**.


2. Give the new map project a name in the **Name** field. For example, **Suzhou Bus Stop Map**.

  
3. Then for **Location**, select the project folder we created earlier. Note that by default, ArcGIS Pro stores map projects locally on your computer.


4. Once **Name** and **Location** are set, click **OK**.


5. This will open the project workspace, where you can start working on.

   
6. The interface of ArcGIS Pro includes:
   1) Project tab
   2) The Command Search box
   3) The ribbon
   4) Contents pane
   5) Table view
   6) Catalog pane


7. If any panes are missing, you can reopen them by going to **View > Pane Sets**.


## Change basemap

1. Go to the Map tab, then click Basemap.

   
2. Choose a new style from the dropdown menu.

  
3. The basemap in the map view will update accordingly.


# Import and Visualize Data

There are multiple ways to add data to a map project in ArcGIS Pro - you can add datasets with location data, upload images, connect to external sources via URL, or create your own sketches directly in the map.

ArcGIS Pro supports a wide range of file and data types, including Shapefile (.shp), File Geodatabase (.gdb), GeoJSON (.geojson / .json), KML/KMZ (.kml, .kmz), CAD files (.dwg, .dxf), GeoTIFF (.tif / .tiff), JPEG/PNG (.jpg, .png), IMG (.img), CSV (.csv), Excel (.xlsx), dBASE (.dbf), text files (.txt), and database connections such as SQL Server and Oracle.

For a full list of data types and items that can be imported into ArcGIS Pro, visit [Supported data types and items](https://doc.esri.com/en/arcgis-pro/latest/help/projects/supported-data-types-and-items.html) by Esri. 

## Shapefile

A shapefile is one of the most common geospatial data formats used in GIS, which stores geographic features (such as points, lines, or polygons) along with their associated attributes.

Despite its name, a shapefile is actually a collection of several related files (e.g., .shp, .shx, .dbf) that must stay together for the data to function properly. 

**suzhou_boundary** is a folder containing a shapefile and its supporting files. It provides provincial-level boundary data for China, with each province represented as a polygon. Let’s add this data to the map!

1. Go to the **Map** tab, click **Add Data**.

  
2. Locate the project folder, then open **suzhou_boundary** folder.

  
3. Select the **citybase.shp** file and click **OK**.

  
4. Now, in the **Contents** pane, you should see the **citybase** layer.

  
5. For the imported data layer, you may toggle the visibility.

  
6. To change the visuals setting of the layer, select and right-click the layer, click **Symbology**.

  
7. You can choose an existing style for the features under the **Gallery** tab, or customize colors, symbols, and other settings under the **Properties** tab.

  
8. Remember to click **Apply** before closing the settings.

## Table
is a data table containing information about every airport in China, including their names,  addresses, coordinates, and year of construction. Let’s map this data on the map! Before we begin, make sure you have downloaded the file to your computer.

1. First, drag and drop the **suzhou_bus_stops.csv** and **suzhou_population.csv** into the **Contents** pane. We will use **suzhou_population.csv** later

  
2. Go to the **Map** tab, click **XY Table to Point**.
   

3. In the **Geoprocessing** pane, for **Input Table**, select **suzhou_bus_stops.csv**.

   
4. For **Output Feature Class**, keep the default name **suzhou_bus_stops**.

   
5. For **X Field**, select **Longitude**.

   
6. For **Y Field**, select **Latitude**.

    
7. Make sure **GCS_WGS_1984** is selected under the **Coordinate System**.

    
8. Click **Run**.

    
9. Now, in the **Contents** pane, you should see the **suzhou_bus_stops** layer.

## Living Atlas

You may also import data from ArcGIS’s Living Atlas into your project. ArcGIS Living Atlas is a collection of ready-to-use datasets provided by Esri, including maps, boundaries, population data, environmental layers, and satellite imagery.

In this tutorial, we will not use data from the Living Atlas. However, this section is introduced to give you an understanding of how to obtain additional data directly within ArcGIS Pro when needed.

1. To access Living Atlas, go to the **Map** tab, click **Add Data > Browse**.

   
2. In the top-right corner of the pop up where it says **Search Living Atlas**, enter **“China”**.

  
3. In the result list, click the first option **China Prefecture Boundaries**.

   
4. Now, in the **Contents** pane, you should see the **CHN_Prefectures** layer.

   
5. Next, make sure the **CHN_Prefectures** layer is selected, right-click and select **Remove** from the menu.

## Other data types

For more instructions on importing different types of data, visit [Add data to a project](https://doc.esri.com/en/arcgis-pro/latest/get-started/add-data-to-your-project.html).

# Geoprocessing

## Join population and city data

1. In the Command Search box, enter **“Join Field”**, select **Join Field (Data Management Tools)**.


2. In the **Geoprocessing** pane, select **citybase** for **Input Table** and **ename** for **Input Field**.

   
3. Select **suzhou_population.csv** for **Join Table** and **Area** for **Join Field**.

   
4. For **Transfer Method**, select **Select transfer fields**, and for **Transfer Fields**, select **Population**.

   
5. For **Index Join Fields**, select **Do not add indexes**.

    
6. Click **Run**.
    
    
7. Now, select **citybase** in the **Contents** pane and right-click, and select **Open (Table)**.

    
8. **“Population”** field should now be joined to the dataset.


## Buffer

The Buffer tool creates polygons around input features at a specified distance, and the dissolve tool is used to combine all buffer polygons into a single layer and merge any overlapping areas. 

In this tutorial, we will first create 500-meter buffers around each bus stop to visualize the current service areas (areas that are accessible to the bus stops). We will also set the Dissolve Type within the Buffer tool to combine all buffers into a single service area layer.

1. In the Command Search box, enter **“Buffer”**, select **Buffer (Analysis Tools)**.

  
2. In the **Geoprocessing** pane, select **suzhou_bus_stops** for **Input Features**. This will automatically name the **Output Feature Class** by adding **“_Buffer”** to the end. You can change the name if needed, but in this tutorial we will keep the default.


3. Set **Distance [value or field]** to **500, Linear Unit** to **Meters**.


4. Keep **Planar** as the **Method**, and set **Dissolve Type** to **Dissolve all output features into a single feature**. This will help us create a layer that merges all buffers into one continuous area.

 
5. Click **Run**.

  
6. Once the analysis is completed, a new layer **suzhou_bus_stops_Buffer** should appear in the **Contents** pane. Uncheck the **suzhou_bus_stops** layer, and the map view should look like the one shown below.


## Intersect Tool

The Intersect tool combines multiple layers and retains only the areas where they overlap. It also preserves attributes from both input layers, making it useful for spatial analysis.

We are going to create a new layer showing only the buffer areas that fall within each district, along with the corresponding district information. This output can then be used to calculate coverage for each district.

1. In the Command Search box, enter **“Intersect”**, select **Intersect (Analysis Tools)**.

   
2. In the **Geoprocessing** pane, select **suzhou_bus_stops_Buffer** and **citybase** for **Input Features**.

   
3. Next, for **Output Feature Class**, let's change the name to **suzhou_bus_stops_by_district**.

   
4. Set **Attributes To Join** to **All attributes**.

   
5. Set **Output Type** to **Same as input**.

    
6. Click **Run**.

    
7. Once the analysis is completed, a new layer **suzhou_bus_stops_by_district** should appear in the **Contents** pane. Right-click and select **Attribute Table** from the menu.

    
8. Make sure the **Population** and **Shape_Area** fields are included in the attribute table, as they will be used in later steps.


## Calculate Coverage per District

1. In the table view, click **Add**.

   
2. Create a new field named **Coverage_pc** and set the data type to **Double**.

   
3. Click the close icon of the new field tab, and **Save**.

   
4. In the table view, click Calculate.

   
5. Make sure **Coverage_pc** is selected under **Field Name**, and **Python** under **Expression Type**.

    
6. Next, copy and paste **“!Shape_Area! / !Population!”** in the **Coverage_pc** = field.

    
7. Click **Apply**, then **OK**.

    
8. You may notice a series of 0 values in the **Coverage_pc** field. This does not mean the calculation is incorrect; rather, the values are very small and are being rounded. You can double-click any cell to view the full value.

    
9. Since our goal is to identify which districts in Suzhou have the least bus service coverage relative to population, we can sort the field. Right-click the **Coverage_pc** field and select **Sort Ascending**.

    
10. The table will now be ordered from lowest to highest coverage. From this, we can see that the three districts with the lowest bus service coverage per capita are Wuzhong, Huqiu, and Gusu District.


## Join coverage with citybase data

We can further join the coverage data with the city boundary dataset to create a choropleth map that visualizes variations in bus stop service coverage across different districts in Suzhou. 

1. In the Command Search box, enter **“Join Field”**, select **Join Field (Data Management Tools)**.

   
2. In the **Geoprocessing** pane, select **citybase** for **Input Table** and **ename** for **Input Field**.

   
3. Select **suzhou_bus_stops_by_district** for **Join Table** and **ename** for **Join Field**.

   
4. For **Transfer Method**, select **Select transfer fields**, and for **Transfer Fields**, select **Coverage_pc**.

   
5. For **Index Join Fields**, select **Do not add indexes**.

    
6. Click **Run**.

    
7. Once the analysis is completed, go to the Contents pane and make sure only the **citybase** is visible. Select it, then right-click and select **Attribute Table** from the menu.

    
8. In the table, right-click and select **Fields**. Rename **Coverage_p** to **Coverage by population (%)**.


9. Still in the table, click on the ellipsis (three-dot) icon next to **Numeric** under **Number Format**, lower the decimal places to **1**, click **OK** when finished.

    
10. Click the close icon of the **Fields** tab, and click **Save** before closing.

    
11. Click **Calculate**, select **Coverag_p** as **Field Name**, then for the equation, write down **“!Coverage_p!*1000000 * 100”**, then click **Apply** and **OK**. This step converts the unit from per square kilometer (km²) to per square meter (m²) and expresses it as a percentage.

    
12. Go to the **Contents** pane again, select **citybase**, then right-click and select **Symbology** from the menu.

    
13. Click the arrow next to the **Single Symbol** dropdown, and switch to **Graduated Color**s.

    
14. For **Field**, switch to **Coverage_p**, and choose a color scheme to **Purple-Blue (Continuous)**.

    
15. If the current color scheme is reversed (for example, if you want areas with the least coverage to appear in the darkest color), you can adjust this by going to the **Classes** tab, **More > Reverse symbol order**.

    
16. You may further customize the color distribution under the **Histogram** or **Scale** tabs. For example, in the **Histogram** tab, double-click on the third breakpoint and enter **25.2**. After doing so, you will see that three districts (Wuzhong, Huqiu, and Gusu) are displayed in darkest colors, indicating that they have the lowest coverage rates.

# Save the project
1. To save the project, go to the top-left corner, and click **Save Project** icon.

  
2. The project will be stored in your computer, under **Documents > ArcGIS > Projects > [Project Name]**.

3. If you want to save another copy of it, go to **Project > Save Project As**. Choose the location you want to save the project and click **Save**. This is especially useful when you are not using your own computer (e.g., a school computer) and want to keep a copy of your work.

# Export map

ArcGIS Pro supports the creation and export of maps with essential layout elements such as a title, legend, scale bar, and north arrow. [Example final map](</ArcGIS/ArcGIS Pro/Example final map.pdf>) is the one we will create and export.

## New Layout

1. Go to **Insert > New Layout** and choose a page size (e.g., Landscape, 8.5 × 11").

   
2. In the blank layout, go to the Insert tab again, click **Map Frame**, and select **Map** (the project you just created).

   
3. Draw a box on the page to define where the map will be placed, the map will automatically appear in the layout. Be sure to leave enough space for essential elements (the title, legend, scale bar, and north arrow).

   
4. To adjust the map’s extent, right-click the map frame, select **Activate**, and then pan or zoom as needed.


5. When you have finished adjusting the map extent, go to **Layout > Close Activation**.

## Map Title
1. Go to **Insert > Dynamic Text**, select **Name of Map**, and draw a rectangle in the layout. Double-click the text box to rename the map to **“Bus Stop Service in Suzhou.”**

   
2. You can also edit the title in the **Element** pane on the right by updating the text under **Text**.

   
3. Go to the **Text Symbol** tab, where you can customize the appearance of the map title (e.g., font, size, color, and alignment).

   
4. To delete any elements, right-click on the element and select **Delete** from the menu.


## North Arrow and Legend

1. Click **North Arrow**, select one from the menu, and draw a box in the layout or map to place it.

   
2. Next, repeat the same steps to add a scale bar, and move it to a suitable place on the map.

   
3. Again, repeat the same steps to add a legend.

   
4. Go to the **Element** pane to edit the legend. First, under the **Legend** tab, uncheck **Show** next to **Title**.

   
5. Then, click on **show property…** button, uncheck **Layer Name** under **Show**.

  
6. Go to the **Text Symbol** tab to edit the text font.

    
7. For convenience, you can enable **Auto Apply** in the bottom-left corner to preview changes instantly.


## Additional Text 

1. If you have supplementary information to add other than the essential map elements (e.g., data source, cartographer name, date of creation), you may go to **Dynamic Text**, then select **Description**.

   
2. Draw a box under the scale bar and add the text to it: “Source: 2020 Census, ChinaGeo-Explorer Cartographer: XXXX Date: 2026-04-22” separated by enter line space.

## Grid

3. Grids are useful for indicating geographic location. To add one, select the map in the layout first, then go to the **Insert** tab, and click **Grid** under **Map Frame** group.

   
4. Select **Black Vertical Label Graticule**.

   
5. Go to the **Element** pane, click the arrow icon and switch from **Map Grid** to **Gridlines**.

   
6. To hide the grid lines across the map, switch the color from Black to No color.

    
7. Note that all elements added to the layout will appear in the **Contents** pane. You may double-click on each element to rename it.


## Export to PDF

1. Once layout is ready, go to **Share** tab > **Export Layout**.
     
2. Select Flatted PDF.

   
3. Under **File**, you can choose the export file format. In this tutorial, we will keep the format as PDF.

   
4. Click on the folder icon, locate the tutorial folder, name the file as **“Bus Stop Service in Suzhou”** then click **OK**.

   
5. For **Compression**, uncheck **Output as image** and change **Vector resolution** from 150 to 300 DPI.

    
6. For **Font**, ensure that **Embed fonts** is enabled. This preserves text as selectable and searchable in the exported PDF; otherwise, the text will be preserved as part of the image. Then click **Export**.

    
7. Locate the tutorial folder and open the **Bus Stop Service in Suzhou.pdf** file. You should now be able to view the map and select the text within it.


# Export data

In ArcGIS Pro, you can export a layer or dataset to save a copy of your processed data for further analysis, sharing, or long-term use. Note that items created and saved within the project are typically stored in a geodatabase, so the output format will appear as a .gdb by default, which can be opened directly in ArcGIS Pro. 

## Geodatabase

1. Go back to the **Map** tab in ArcGIS Pro.

   
2. In the **Contents** pane, select the **suzhou_bus_stops_by_district** layer, right-click and select **Data > Export Table**.

3. Make sure the **Input Table** and **Output Table** is set correctly, then click **OK**.

4. The file will be automatically stored in your computer, under **Documents > ArcGIS > Projects > [Project Name]**.

## Table 

1. In the Command Search box, enter **“table to”**, select **Table to Excel (Conversion Tools)**. 


2. In the **Geoprocessing** pane, select **suzhou_bus_stops_by_district** as **Input Table**. 


3. For **Output Excel File**, click on the folder icon, locate the tutorial folder, and name it as 
**“bus_stops_coverage”**. 

4. Click **Run**. 

5. Once the export is complete, you should find the exported Excel file in your tutorial folder.


## Shapefile

For items created within a map project, you can use the **Feature Class to Shapefile** tool to export it as shapefile directly. 

1. In the Command Search box, search for **Feature Class to Shapefile (Conversion Tools)**. 


2. In the **Geoprocessing** pane, select **suzhou_bus_stops_by_district** as **Input Features**. 


3. For **Output Folder**, click on the folder icon, locate the tutorial folder, and click **OK**. 


4. Click **Run**. 

5. Once the export is complete, you should find the exported shapefile in your tutorial folder. Note that GIS recognizes a shapefile only when all its component files share the same name (e.g., .shp, .shx, .dbf). These files must be kept together in the same folder; otherwise, the shapefile may not open properly.


# Resources

ArcGIS Pro offers a wide range of tools for visualizing and analyzing geospatial data, and this tutorial only covers some of them. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

- [ArcGIS Pro Resources](https://www.esri.com/en-us/arcgis/products/arcgis-pro/resources) by Esri; 
- [ArcGIS Pro Introduction](https://guides.library.duke.edu/arcgispro) by Duke Library; 
- [ArcGIS Pro quick-start tutorials](https://pro.arcgis.com/en/pro-app/latest/get-started/pro-quickstart-tutorials.htm) by Esri; 
- [ArcGIS Pro Community](https://community.esri.com/t5/arcgis-pro/ct-p/arcgis-pro) for browsing resources, sharing knowledge, and connecting with other users. 

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei <siti.lei@dukekunshan.edu.cn> for further support.


















