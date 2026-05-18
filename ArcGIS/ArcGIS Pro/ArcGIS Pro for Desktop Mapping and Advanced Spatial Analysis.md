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

- [x] run
- [ ] dance
- [x] drink
- [ ] write


























