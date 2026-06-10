# **ArcGIS Pro for Desktop Mapping and Advanced Spatial Analysis**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*  

*Last updated: June 10, 2026*

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

- [Intersect](#intersect-tool)

- [Calculate coverage per district](#calculate-coverage-per-district)

- [Join coverage with citybase data](#join-coverage-with-citybase-data )

**[Save the project ](#save-the-project)**

**[Export map ](#export-map )**

- [New layout ](#new-layout)

- [Map title ](#map-title)

- [North arrow and legend ](#north-arrow-and-legend)

- [Additional text](#additional-text)

- [Grid ](#grid)

- [Export to PDF](#export-to-pdf)

**[Export data ](#export-data)**

- [Geodatabase ](#geodatabase)

- [Table](#table-1)

- [Shapefile](#shapefile-1)

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

[The sample dataset](</ArcGIS/ArcGIS Pro/Dataset/ArcGIS Pro Tutorial Sample Dataset.zip>) is sourced from [China Geo-Explore](https://login.proxy.lib.duke.edu/login?url=http://chinageoexplorer.com/)  and [Figshare](https://pmc.ncbi.nlm.nih.gov/articles/PMC12886901/), and the data has been cleaned and edited for the purpose of demonstration. The folder contains three files:

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
<p align="center"><img width="700"  alt="image28" src="https://github.com/user-attachments/assets/33d6f4f9-b224-48c1-b8c8-f7331f28b22c" />

3. Move the sample datasets to this folder.
   
4. In the folder, right-click one ZIP file and select **Extract All…** to unzip it. Repeat the same steps for the other file.
<p align="center"><img width="700"  alt="image65" src="https://github.com/user-attachments/assets/feb6cd3f-da20-431e-a1ef-3693ec1e0135" />

5. Open **suzhou_boundary** folder and make sure the file contents match those shown in the image below. Note that when importing a shapefile into the project, the accompanying files in the folder are **required** to support it. Without them, the shapefile may not open properly.
<p align="center"><img width="400"  alt="image1" src="https://github.com/user-attachments/assets/c56c3f30-99e6-4341-b21d-d5036960d38c" />

6. After extracting, delete the ZIP file from the folder.

## Sign in to ArcGIC Pro

1. Open ArcGIS Pro on your computer. 
2. In the pop up, select **Your ArcGIS organization’s URL**, enter **dukeuniv**, then click **Continue**.
<p align="center"><img width="400" alt="image29" src="https://github.com/user-attachments/assets/17bf2204-83c7-4dd1-a204-b4ae9d849b07" />

3. Click the **Duke University** button.
<p align="center"><img width="400" src="https://github.com/user-attachments/assets/fef41803-1565-45a6-bf87-819029573d17" />

4. Sign in with your NetID. If you are using your personal computer, you may check **Sign in automatically** in the bottom-left corner.
<p align="center"><img width="400"  alt="image61" src="https://github.com/user-attachments/assets/342855a3-d29d-4506-b7a4-d7cde52992f3" />

5. Once signed in, you will be directed to the ArcGIS Pro **Home** page.

## Create a map project

1. In the **Home** page, click on **Map**.
<p align="center"><img width="514" alt="image19" src="https://github.com/user-attachments/assets/a265f578-860c-4a8e-b6f0-9747afdbac1b" />

2. Give the new map project a name in the **Name** field. For example, **Suzhou Bus Stop Map**.
<p align="center"><img width="514" height="262" alt="image53" src="https://github.com/user-attachments/assets/e6c58fa8-96cd-4f04-9497-1e6c5ed282fb" />

3. Then for **Location**, select the project folder we created earlier. Note that by default, ArcGIS Pro stores map projects locally on your computer.
<p align="center"><img width="514" height="262" alt="image4" src="https://github.com/user-attachments/assets/5ab315a6-38cf-4b76-8da5-4508e7905aa7" />

4. Once **Name** and **Location** are set, click **OK**.
<p align="center"><img width="514" height="262" alt="image2" src="https://github.com/user-attachments/assets/19a6344a-de9e-42d7-9ada-35d47787e613" />

5. This will open the project workspace, where you can start working on.
<p align="center"><img width="800"  alt="image21" src="https://github.com/user-attachments/assets/47669a4a-8dea-4d1c-8883-2105cc698f8d" />
 
6. The interface of ArcGIS Pro includes:
   1) Project tab
   2) The Command Search box
   3) The ribbon
   4) Contents pane
   5) Table view
   6) Catalog pane
<p align="center"><img width="650"  alt="image36" src="https://github.com/user-attachments/assets/53afe0e8-3078-4670-9422-444ca8c8d273" />

7. If any panes are missing, you can reopen them by going to **View > Pane Sets**.
<p align="center"><img width="500"  alt="image52" src="https://github.com/user-attachments/assets/cb63857d-4470-4bfb-bb80-e09469c0b69e" />

## Change basemap

1. Go to the **Map** tab, then click **Basemap**.
<p align="center"><img width="500"  alt="image32" src="https://github.com/user-attachments/assets/c885916f-7e2b-4e76-8ede-c04b7bc107d0" />
   
2. Choose a new style from the dropdown menu.
<p align="center"><img width="500"  alt="image57" src="https://github.com/user-attachments/assets/e1be7428-86b7-4b69-9796-5d5ebecd390c" />
  
3. The basemap in the map view will update accordingly.
<p align="center"><img width="800"  alt="image47" src="https://github.com/user-attachments/assets/ce979bbd-9d08-4a1d-a103-04f86795afee" />

# Import and Visualize Data

There are multiple ways to add data to a map project in ArcGIS Pro - you can add datasets with location data, upload images, connect to external sources via URL, or create your own sketches directly in the map.

ArcGIS Pro supports a wide range of file and data types, including Shapefile (.shp), File Geodatabase (.gdb), GeoJSON (.geojson / .json), KML/KMZ (.kml, .kmz), CAD files (.dwg, .dxf), GeoTIFF (.tif / .tiff), JPEG/PNG (.jpg, .png), IMG (.img), CSV (.csv), Excel (.xlsx), dBASE (.dbf), text files (.txt), and database connections such as SQL Server and Oracle.

For a full list of data types and items that can be imported into ArcGIS Pro, visit [Supported data types and items](https://doc.esri.com/en/arcgis-pro/latest/help/projects/supported-data-types-and-items.html) by Esri. 

## Shapefile

A shapefile is one of the most common geospatial data formats used in GIS, which stores geographic features (such as points, lines, or polygons) along with their associated attributes.

Despite its name, a shapefile is actually a collection of several related files (e.g., .shp, .shx, .dbf) that must stay together for the data to function properly. 

**suzhou_boundary** is a folder containing a shapefile and its supporting files. It provides provincial-level boundary data for China, with each province represented as a polygon. Let’s add this data to the map!

1. Go to the **Map** tab, click **Add Data**.
<p align="center"><img width="500"  alt="image43" src="https://github.com/user-attachments/assets/4a33d27d-9fb3-41d5-8bae-80bf236b46be" />
  
2. Locate the project folder, then open **suzhou_boundary** folder.
<p align="center"><img width="500"  alt="image71" src="https://github.com/user-attachments/assets/c179fa28-1a03-4a9e-a3e0-7e742a35a137" />
 
3. Select the **citybase.shp** file and click **OK**.
<p align="center"><img width="500"  alt="image73" src="https://github.com/user-attachments/assets/3e720bff-d4de-46fe-a915-c14975ea7f35" />
  
4. Now, in the **Contents** pane, you should see the **citybase** layer.
<p align="center"><img width="300"  alt="image23" src="https://github.com/user-attachments/assets/ff90b2eb-51c6-47c6-8a23-19d60a663653" />
  
5. For the imported data layer, you may toggle the visibility.
<p align="center"><img width="300"  alt="image69" src="https://github.com/user-attachments/assets/61f98aa7-824a-4da1-9534-c12f249bf80b" />
  
6. To change the visuals setting of the layer, select and right-click the layer, click **Symbology**.
<p align="center"><img width="300"  alt="image86" src="https://github.com/user-attachments/assets/e377388f-f483-4b5b-91bf-c38931cf0edb" />
 
7. You can choose an existing style for the features under the **Gallery** tab, or customize colors, symbols, and other settings under the **Properties** tab.
<p align="center"><img width="400"  alt="image93" src="https://github.com/user-attachments/assets/c4a820a5-f290-425f-874b-d384a2dfc42d" />

8. Remember to click **Apply** before closing the settings.
<p align="center"><img width="400"  alt="image75" src="https://github.com/user-attachments/assets/e31ba5df-c97b-4ac1-90bc-fd79166089e2" />

## Table
is a data table containing information about every airport in China, including their names,  addresses, coordinates, and year of construction. Let’s map this data on the map! Before we begin, make sure you have downloaded the file to your computer.

1. First, drag and drop the **suzhou_bus_stops.csv** and **suzhou_population.csv** into the **Contents** pane. We will use **suzhou_population.csv** later
<p align="center"><img width="300"  alt="image95" src="https://github.com/user-attachments/assets/94994a5f-89fd-4775-bc4b-62c395a866b7" />
 
2. Go to the **Map** tab, click **XY Table to Point**.
<p align="center"><img width="600"  alt="image80" src="https://github.com/user-attachments/assets/492f7917-4374-47ba-86cf-8aac98506fbc" />
   
3. In the **Geoprocessing** pane, for **Input Table**, select **suzhou_bus_stops.csv**.
 
4. For **Output Feature Class**, keep the default name **suzhou_bus_stops**.
<p align="center"><img width="400"  alt="image35" src="https://github.com/user-attachments/assets/725b7888-f774-4d77-bd3d-bba29cbe4415" />
   
5. For **X Field**, select **Longitude**.

6. For **Y Field**, select **Latitude**.
 
7. Make sure **GCS_WGS_1984** is selected under the **Coordinate System**.
<p align="center"><img width="400"  alt="image16" src="https://github.com/user-attachments/assets/745d1fc0-6c43-47f3-8d39-f5ab75c3de81" />
   
8. Click **Run**.
<p align="center"><img width="192" height="101" alt="image55" src="https://github.com/user-attachments/assets/ee894c45-223e-4414-ae20-68ea9e70e452" />
  
9. Now, in the **Contents** pane, you should see the **suzhou_bus_stops** layer.
<p align="center"><img width="800" alt="image22" src="https://github.com/user-attachments/assets/3907fd4a-45c0-4b15-a32f-c520dcffcbf1" />

## Living Atlas

You may also import data from ArcGIS’s Living Atlas into your project. ArcGIS Living Atlas is a collection of ready-to-use datasets provided by Esri, including maps, boundaries, population data, environmental layers, and satellite imagery.

In this tutorial, we will not use data from the Living Atlas. However, this section is introduced to give you an understanding of how to obtain additional data directly within ArcGIS Pro when needed.

1. To access Living Atlas, go to the **Map** tab, click **Add Data > Browse**.
<p align="center"><img width="800"  alt="image78" src="https://github.com/user-attachments/assets/ba606e3e-c211-4203-833b-ed7b7141eb0c" />

2. In the top-right corner of the pop up where it says **Search Living Atlas**, enter **“China”**.
<p align="center"><img width="500" alt="image82" src="https://github.com/user-attachments/assets/c7299412-7f4e-4598-9800-6e36d8f2cc52" />
 
3. In the result list, click the first option **China Prefecture Boundaries**.
<p align="center"><img width="500" alt="image14" src="https://github.com/user-attachments/assets/1c8b345c-dfe2-4a3c-8dc9-c011612e1f0a" />
 
4. Now, in the **Contents** pane, you should see the **CHN_Prefectures** layer.
<p align="center"><img width="317" height="490" alt="image70" src="https://github.com/user-attachments/assets/a5273c64-7e71-40f6-bce7-09d7f5e61624" />

5. Next, make sure the **CHN_Prefectures** layer is selected, right-click and select **Remove** from the menu.
<p align="center"><img width="392" height="396" alt="image83" src="https://github.com/user-attachments/assets/aef96efd-5a5b-4ac0-be2e-106bf3980e8d" />

## Other data types

For more instructions on importing different types of data, visit [Add data to a project](https://doc.esri.com/en/arcgis-pro/latest/get-started/add-data-to-your-project.html).

# Geoprocessing

## Join population and city data

1. In the Command Search box, enter **“Join Field”**, select **Join Field (Data Management Tools)**.
<p align="center"><img width="304" height="366" alt="image3" src="https://github.com/user-attachments/assets/bde1894b-fab3-4279-b4d2-64d2a3d4bcc7" />

2. In the **Geoprocessing** pane, select **citybase** for **Input Table** and **ename** for **Input Field**.
<p align="center"><img width="450"  alt="image66" src="https://github.com/user-attachments/assets/2566809c-7a8a-4f99-b4a7-d031a5d198bf" />

3. Select **suzhou_population.csv** for **Join Table** and **Area** for **Join Field**.
<p align="center"><img width="450" alt="image77" src="https://github.com/user-attachments/assets/2a1ccaec-5fe3-4b5b-a4de-719956f67a8e" />
 
4. For **Transfer Method**, select **Select transfer fields**, and for **Transfer Fields**, select **Population**.
   
5. For **Index Join Fields**, select **Do not add indexes**.
<p align="center"><img width="300"  alt="image109" src="https://github.com/user-attachments/assets/727ca093-a321-4298-b254-533f5a4a7ef1" />

6. Click **Run**.
       
7. Now, select **citybase** in the **Contents** pane and right-click, and select **Open (Table)**.
<p align="center"><img width="450"  alt="image49" src="https://github.com/user-attachments/assets/84dd00b9-334a-41dd-951b-c769194e1d75" />
    
8. **“Population”** field should now be joined to the dataset.
<p align="center"><img width="350"  alt="image74" src="https://github.com/user-attachments/assets/8e15102d-bc6f-456a-b970-9956396cb393" />

## Buffer

The Buffer tool creates polygons around input features at a specified distance, and the dissolve tool is used to combine all buffer polygons into a single layer and merge any overlapping areas. 

In this tutorial, we will first create 500-meter buffers around each bus stop to visualize the current service areas (areas that are accessible to the bus stops). We will also set the Dissolve Type within the Buffer tool to combine all buffers into a single service area layer.

1. In the Command Search box, enter **“Buffer”**, select **Buffer (Analysis Tools)**.
<p align="center"><img width="300"  alt="image30" src="https://github.com/user-attachments/assets/3f9d0f49-98d6-4b7d-ad5d-da6a053506ed" />
 
2. In the **Geoprocessing** pane, select **suzhou_bus_stops** for **Input Features**. This will automatically name the **Output Feature Class** by adding **“_Buffer”** to the end. You can change the name if needed, but in this tutorial we will keep the default.
<p align="center"><img width="300" alt="image33" src="https://github.com/user-attachments/assets/837acc7f-6b56-4af5-ac06-697f5362587d" />

3. Set **Distance [value or field]** to **500, Linear Unit** to **Meters**.
<p align="center"><img width="500"  alt="image44" src="https://github.com/user-attachments/assets/c026c8b3-2dcd-47cd-9330-922be27d4a93" />

4. Keep **Planar** as the **Method**, and set **Dissolve Type** to **Dissolve all output features into a single feature**. This will help us create a layer that merges all buffers into one continuous area.
<p align="center"><img width="300"  alt="image13" src="https://github.com/user-attachments/assets/20e24ec4-28d4-44e8-a46c-d33c67e58156" />

5. Click **Run**.

6. Once the analysis is completed, a new layer **suzhou_bus_stops_Buffer** should appear in the **Contents** pane. Uncheck the **suzhou_bus_stops** layer, and the map view should look like the one shown below.
<p align="center"><img width="800"  alt="image11" src="https://github.com/user-attachments/assets/421676f1-1d26-4edc-af78-1956b101dfb8" />

## Intersect

The Intersect tool combines multiple layers and retains only the areas where they overlap. It also preserves attributes from both input layers, making it useful for spatial analysis.

We are going to create a new layer showing only the buffer areas that fall within each district, along with the corresponding district information. This output can then be used to calculate coverage for each district.

1. In the Command Search box, enter **“Intersect”**, select **Intersect (Analysis Tools)**.
<p align="center"><img width="335" height="505" alt="image48" src="https://github.com/user-attachments/assets/de2aaaeb-5fd3-439d-a976-63d137fb7aa8" />
   
2. In the **Geoprocessing** pane, select **suzhou_bus_stops_Buffer** and **citybase** for **Input Features**.
<p align="center"><img width="500" alt="image72" src="https://github.com/user-attachments/assets/4e772bb2-2ad6-48fb-a579-22863841c7ef" />
 
3. Next, for **Output Feature Class**, let's change the name to **suzhou_bus_stops_by_district**.
<p align="center"><img width="500"  alt="image81" src="https://github.com/user-attachments/assets/7a1afee1-4b52-4439-872d-a1b8f760fc05" />

4. Set **Attributes To Join** to **All attributes**.
<p align="center"><img width="500"  alt="image37" src="https://github.com/user-attachments/assets/061c35ce-1b59-405a-a170-e22b9ee511d0" />
  
5. Set **Output Type** to **Same as input**.
<p align="center"><img width="332" height="396" alt="image51" src="https://github.com/user-attachments/assets/7c78d3b3-0fff-4f30-a247-ab578b363c1c" />
 
6. Click **Run**.
    
7. Once the analysis is completed, a new layer **suzhou_bus_stops_by_district** should appear in the **Contents** pane. Right-click and select **Attribute Table** from the menu.
<p align="center"><img width="500"  alt="image91" src="https://github.com/user-attachments/assets/32d3ee48-c73f-4412-9b27-578eac86f404" />
    
8. Make sure the **Population** and **Shape_Area** fields are included in the attribute table, as they will be used in later steps.
<p align="center"><img width="700"  alt="image103" src="https://github.com/user-attachments/assets/de15071d-1c8c-4f59-b7a4-039e6fe1938c" />

## Calculate coverage per district

1. In the table view, click **Add**.
<p align="center"><img width="700"  alt="image6" src="https://github.com/user-attachments/assets/7127d99e-6dda-4814-993f-858f30bbb921" />

2. Create a new field named **Coverage_pc** and set the data type to **Double**.
   
3. Click the close icon of the new field tab, and **Save**.
<p align="center"><img width="350"  alt="image62" src="https://github.com/user-attachments/assets/4dabaae1-8808-44cd-a0af-1009805f00e8" />

4. In the table view, click Calculate.
<p align="center"><img width="550"  alt="image98" src="https://github.com/user-attachments/assets/abdb0871-e7c7-4ae0-903c-da5b28e11df0" />
  
5. Make sure **Coverage_pc** is selected under **Field Name**, and **Python** under **Expression Type**.
<p align="center"><img width="350"  alt="image50" src="https://github.com/user-attachments/assets/c4416a0d-8193-40a4-ae45-a172158127b2" />
    
6. Next, copy and paste **“!Shape_Area! / !Population!”** in the **Coverage_pc** = field.
<p align="center"><img width="350"  alt="image64" src="https://github.com/user-attachments/assets/5319f385-4e73-4000-a27f-cbc95495f12a" />

7. Click **Apply**, then **OK**.
<p align="center"><img width="350"  alt="image96" src="https://github.com/user-attachments/assets/7e6953ca-848f-4a7f-8124-1bb7b2deed7b" />
 
8. You may notice a series of 0 values in the **Coverage_pc** field. This does not mean the calculation is incorrect; rather, the values are very small and are being rounded. You can double-click any cell to view the full value.
<p align="center"><img width="161" height="51" alt="image97" src="https://github.com/user-attachments/assets/11f16713-489d-434b-8e58-52bcf4a44d34" />
  
9. Since our goal is to identify which districts in Suzhou have the least bus service coverage relative to population, we can sort the field. Right-click the **Coverage_pc** field and select **Sort Ascending**.
<p align="center"><img width="280"  alt="image60" src="https://github.com/user-attachments/assets/57232b41-2981-4d68-9699-47a053e0e5f7" />
 
10. The table will now be ordered from lowest to highest coverage. From this, we can see that the three districts with the lowest bus service coverage per capita are Wuzhong, Huqiu, and Gusu District.
<p align="center"><img width="700"  alt="image25" src="https://github.com/user-attachments/assets/35344e88-9229-4d0b-8e8f-849a6780e3ff" />

## Join coverage with citybase data

We can further join the coverage data with the city boundary dataset to create a choropleth map that visualizes variations in bus stop service coverage across different districts in Suzhou. 

1. In the Command Search box, enter **“Join Field”**, select **Join Field (Data Management Tools)**.
<p align="center"><img width="350"  alt="image12" src="https://github.com/user-attachments/assets/23140127-cb79-4c96-a329-e1e1d8ee4086" />
  
2. In the **Geoprocessing** pane, select **citybase** for **Input Table** and **ename** for **Input Field**.
<p align="center"><img width="450"  alt="image7" src="https://github.com/user-attachments/assets/f1cc2711-1c6e-4de9-95ad-f8c0ba335f2b" />
   
3. Select **suzhou_bus_stops_by_district** for **Join Table** and **ename** for **Join Field**.
<p align="center"><img width="450"  alt="image59" src="https://github.com/user-attachments/assets/b6f78058-3332-43f4-9258-e4263c531ab1" />
 
4. For **Transfer Method**, select **Select transfer fields**, and for **Transfer Fields**, select **Coverage_pc**.
<p align="center"><img width="450" alt="image39" src="https://github.com/user-attachments/assets/05c3a572-abb1-4de7-a838-c60c6373a028" />
 
5. For **Index Join Fields**, select **Do not add indexes**.
<p align="center"><img width="450"  alt="image90" src="https://github.com/user-attachments/assets/8fbb847f-88a1-499e-ba91-7ff9b169d2f8" />
  
6. Click **Run**.

7. Once the analysis is completed, go to the Contents pane and make sure only the **citybase** is visible. Select it, then right-click and select **Attribute Table** from the menu.
<p align="center"><img width="450"  alt="image27" src="https://github.com/user-attachments/assets/25800ee9-5e5d-4f45-92e0-fb20904daf23" />
    
8. In the table, right-click and select **Fields**. Rename **Coverage_p** to **Coverage by population (%)**.
<p align="center"><img width="700"  alt="image18" src="https://github.com/user-attachments/assets/0b6e1913-83dd-460b-934c-3bd5c60c7370" />

9. Still in the table, click on the ellipsis (three-dot) icon next to **Numeric** under **Number Format**, lower the decimal places to **1**, click **OK** when finished.
<p align="center"><img width="350"  alt="image100" src="https://github.com/user-attachments/assets/82e6f367-2b6e-467f-95ed-19326fe0ec06" />
    
10. Click the close icon of the **Fields** tab, and click **Save** before closing.
   
11. Click **Calculate**, select **Coverag_p** as **Field Name**, then for the equation, write down **“!Coverage_p!*1000000 * 100”**, then click **Apply** and **OK**. This step converts the unit from per square kilometer (km²) to per square meter (m²) and expresses it as a percentage.
<p align="center"><img width="350"  alt="image105" src="https://github.com/user-attachments/assets/7fcd007b-278a-4f03-b079-f4d56e4231fd" />
 
12. Go to the **Contents** pane again, select **citybase**, then right-click and select **Symbology** from the menu.
<p align="center"><img width="450"  alt="image24" src="https://github.com/user-attachments/assets/895943e9-b9bb-4868-8a6d-119917b99cf6" />

13. Click the arrow next to the **Single Symbol** dropdown, and switch to **Graduated Color**s.
<p align="center"><img width="450"  alt="image94" src="https://github.com/user-attachments/assets/e29c255e-1819-41d0-b015-438428a49453" />
    
14. For **Field**, switch to **Coverage_p**, and choose a color scheme to **Purple-Blue (Continuous)**.
<p align="center"><img width="350"  alt="image54" src="https://github.com/user-attachments/assets/2100813e-f7bf-4eb2-a393-5ee496edd30a" />
  
15. If the current color scheme is reversed (for example, if you want areas with the least coverage to appear in the darkest color), you can adjust this by going to the **Classes** tab, **More > Reverse symbol order**.
<p align="center"><img width="150"  alt="image85" src="https://github.com/user-attachments/assets/37ec2515-d9a1-4ba5-9cd1-df6545f6d18f" />
   
16. You may further customize the color distribution under the **Histogram** or **Scale** tabs. For example, in the **Histogram** tab, double-click on the third breakpoint and enter **25.2**. After doing so, you will see that three districts (Wuzhong, Huqiu, and Gusu) are displayed in darkest colors, indicating that they have the lowest coverage rates.
<p align="center"><img width="500"  alt="image31" src="https://github.com/user-attachments/assets/dfc74bc9-faca-43a7-9e2b-8576585f36fd" />

# Save the project
1. To save the project, go to the top-left corner, and click **Save Project** icon.
<p align="center"><img width="185" height="45" alt="image15" src="https://github.com/user-attachments/assets/28135585-9804-4ab5-8793-10bd51767255" />

2. The project will be stored in your computer, under **Documents > ArcGIS > Projects > [Project Name]**.

3. If you want to save another copy of it, go to **Project > Save Project As**. Choose the location you want to save the project and click **Save**. This is especially useful when you are not using your own computer (e.g., a school computer) and want to keep a copy of your work.

# Export map

ArcGIS Pro supports the creation and export of maps with essential layout elements such as a title, legend, scale bar, and north arrow. [Example final map](</ArcGIS/ArcGIS Pro/Example final map.pdf>) is the one we will create and export.

## New layout

1. Go to **Insert > New Layout** and choose a page size (e.g., Landscape, 8.5 × 11").
<p align="center"><img width="650"  alt="image102" src="https://github.com/user-attachments/assets/960b359a-f79d-4379-91bb-44a4185f973f" />
 
2. In the blank layout, go to the Insert tab again, click **Map Frame**, and select **Map** (the project you just created).
<p align="center"><img width="400" alt="image9" src="https://github.com/user-attachments/assets/08ce62bb-fedf-46d3-bd88-4f5b3be2a111" />
   
3. Draw a box on the page to define where the map will be placed, the map will automatically appear in the layout. Be sure to leave enough space for essential elements (the title, legend, scale bar, and north arrow).
 
4. To adjust the map’s extent, right-click the map frame, select **Activate**, and then pan or zoom as needed.
<p align="center"><img width="300"  alt="image68" src="https://github.com/user-attachments/assets/5ac63cfa-dc9a-461c-a0f7-8869395f5095" />

5. When you have finished adjusting the map extent, go to **Layout > Close Activation**.
<p align="center"><img width="650" height="178" alt="image8" src="https://github.com/user-attachments/assets/7c87836a-d2ee-4b1a-8c80-d811aee339c7" />

## Map title
1. Go to **Insert > Dynamic Text**, select **Name of Map**, and draw a rectangle in the layout. Double-click the text box to rename the map to **“Bus Stop Service in Suzhou.”**
<p align="center"><img width="400"  alt="image108" src="https://github.com/user-attachments/assets/bcb57fa3-6d24-4794-b68a-b14f3fe594aa" />
   
2. You can also edit the title in the **Element** pane on the right by updating the text under **Text**.
<p align="center"><img width="300"  alt="image67" src="https://github.com/user-attachments/assets/8e9416d9-0b4b-4ec4-9298-955a45ed4ecb" />
   
3. Go to the **Text Symbol** tab, where you can customize the appearance of the map title (e.g., font, size, color, and alignment).
<p align="center"><img width="300" height="396" alt="image79" src="https://github.com/user-attachments/assets/5fa6a0e2-9cce-458d-868a-38b188f709ec" />
 
4. To delete any elements, right-click on the element and select **Delete** from the menu.
<p align="center"><img width="300"  alt="image92" src="https://github.com/user-attachments/assets/52596090-43fc-49ec-b3f9-431574714b44" />

## North arrow and legend

1. Click **North Arrow**, select one from the menu, and draw a box in the layout or map to place it.
<p align="center"><img width="250"  alt="image58" src="https://github.com/user-attachments/assets/5fee20a0-98cc-4b2f-bee1-8883539a6bcd" />

2. Next, repeat the same steps to add a scale bar, and move it to a suitable place on the map.

3. Again, repeat the same steps to add a legend.
 
4. Go to the **Element** pane to edit the legend. First, under the **Legend** tab, uncheck **Show** next to **Title**.
<p align="center"><img width="300" alt="image106" src="https://github.com/user-attachments/assets/58bbb687-1521-4dc3-b0ba-9346fd4164c8" />
   
5. Then, click on **show property…** button, uncheck **Layer Name** under **Show**.
<p align="center"><img width="300"  alt="image5" src="https://github.com/user-attachments/assets/5d3b2dc9-bb6a-47cc-88dd-9df51badde8d" />
 
6. Go to the **Text Symbol** tab to edit the text font.
<p align="center"><img width="300"  alt="image56" src="https://github.com/user-attachments/assets/46de54a4-b5b5-46d1-be87-d25f4f27d777" />

7. For convenience, you can enable **Auto Apply** in the bottom-left corner to preview changes instantly.
<p align="center"><img width="200" alt="image46" src="https://github.com/user-attachments/assets/15aa066c-c0bd-4e88-960a-6aefd8d055d2" />

## Additional text 

1. If you have supplementary information to add other than the essential map elements (e.g., data source, cartographer name, date of creation), you may go to **Dynamic Text**, then select **Description**.
<p align="center"><img width="450"  alt="image89" src="https://github.com/user-attachments/assets/033a649a-5ad0-4d46-816d-3d00934901bf" />

2. Draw a box under the scale bar and add the text to it: “Source: 2020 Census, ChinaGeo-Explorer Cartographer: XXXX Date: 2026-04-22” separated by enter line space.

## Grid

3. Grids are useful for indicating geographic location. To add one, select the map in the layout first, then go to the **Insert** tab, and click **Grid** under **Map Frame** group.
<p align="center"><img width="250"  alt="image63" src="https://github.com/user-attachments/assets/28aa5638-07c5-425b-a867-6873a52cd85e" />
 
4. Select **Black Vertical Label Graticule**.
<p align="center"><img width="550"  alt="image107" src="https://github.com/user-attachments/assets/053b565e-d0f4-4bfc-b094-699f36b8d02b" />
   
5. Go to the **Element** pane, click the arrow icon and switch from **Map Grid** to **Gridlines**.
<p align="center"><img width="190"  alt="image42" src="https://github.com/user-attachments/assets/49d9a974-aed5-4bc9-9caf-6ffb1dbf640b" />

6. To hide the grid lines across the map, switch the color from Black to No color.
<p align="center"><img width="300" alt="image84" src="https://github.com/user-attachments/assets/6f4566b5-1ce6-4bce-91d1-96e8d6375e3d" />
    
7. Note that all elements added to the layout will appear in the **Contents** pane. You may double-click on each element to rename it.
<p align="center"><img width="190"  alt="image45" src="https://github.com/user-attachments/assets/9f2d99e8-39bf-4849-952e-c0b6cbf3c6f7" />

## Export to PDF

1. Once layout is ready, go to **Share** tab > **Export Layout**.
     
2. Select Flatted PDF.
<p align="center"><img width="300" alt="image20" src="https://github.com/user-attachments/assets/ecd4adc0-0f86-40ab-9695-6e47398ddc30" />

3. Under **File**, you can choose the export file format. In this tutorial, we will keep the format as PDF.
<p align="center"><img width="133" height="235" alt="image10" src="https://github.com/user-attachments/assets/a0e22544-b329-4c7c-b352-d1d8783c6b86" />

4. Click on the folder icon, locate the tutorial folder, name the file as **“Bus Stop Service in Suzhou”** then click **OK**.
<p align="center"><img width="550"  alt="image26" src="https://github.com/user-attachments/assets/6eeb246f-f54a-484f-b66e-52ea79e16739" />
  
5. For **Compression**, uncheck **Output as image** and change **Vector resolution** from 150 to 300 DPI.
<p align="center"><img width="300"  alt="image34" src="https://github.com/user-attachments/assets/807fe0b3-d773-4118-a929-f7b98e007272" />
   
6. For **Font**, ensure that **Embed fonts** is enabled. This preserves text as selectable and searchable in the exported PDF; otherwise, the text will be preserved as part of the image. Then click **Export**.
<p align="center"><img width="300"  alt="image40" src="https://github.com/user-attachments/assets/1f193357-c0e6-4435-8f68-6018dfd92864" />
  
7. Locate the tutorial folder and open the **Bus Stop Service in Suzhou.pdf** file. You should now be able to view the map and select the text within it.
<p align="center"><img width="800"  alt="image76" src="https://github.com/user-attachments/assets/b42d6ad2-6530-43a6-8b6d-9bc2c15f3c31" />

# Export data

In ArcGIS Pro, you can export a layer or dataset to save a copy of your processed data for further analysis, sharing, or long-term use. Note that items created and saved within the project are typically stored in a geodatabase, so the output format will appear as a .gdb by default, which can be opened directly in ArcGIS Pro. 

## Geodatabase

1. Go back to the **Map** tab in ArcGIS Pro.
<p align="center"><img width="300"  alt="image17" src="https://github.com/user-attachments/assets/0fec830c-5a0c-424e-84a3-032e7c314691" />

2. In the **Contents** pane, select the **suzhou_bus_stops_by_district** layer, right-click and select **Data > Export Table**.

3. Make sure the **Input Table** and **Output Table** is set correctly, then click **OK**.

4. The file will be automatically stored in your computer, under **Documents > ArcGIS > Projects > [Project Name]**.

## Table 

1. In the Command Search box, enter **“table to”**, select **Table to Excel (Conversion Tools)**. 
<p align="center"><img width="300"  alt="image99" src="https://github.com/user-attachments/assets/aa4d3ccb-5373-4c70-8368-a09677691557" />

2. In the **Geoprocessing** pane, select **suzhou_bus_stops_by_district** as **Input Table**. 
<p align="center"><img width="300"  alt="image104" src="https://github.com/user-attachments/assets/a58ea6c2-3e54-4ac7-8af4-4b7f3bcf4f54" />

3. For **Output Excel File**, click on the folder icon, locate the tutorial folder, and name it as 
**“bus_stops_coverage”**. 

4. Click **Run**. 

5. Once the export is complete, you should find the exported Excel file in your tutorial folder.
<p align="center"><img width="550" alt="image38" src="https://github.com/user-attachments/assets/99501a2a-0e01-454b-867a-baead494ca48" />

## Shapefile

For items created within a map project, you can use the **Feature Class to Shapefile** tool to export it as shapefile directly. 

1. In the Command Search box, search for **Feature Class to Shapefile (Conversion Tools)**. 
<p align="center"><img width="300"  alt="image87" src="https://github.com/user-attachments/assets/37a677a2-5983-4368-a3f7-858a9ef4e466" />

2. In the **Geoprocessing** pane, select **suzhou_bus_stops_by_district** as **Input Features**. 
<p align="center"><img width="300"  alt="image101" src="https://github.com/user-attachments/assets/67c34732-72ad-4a6e-a415-19fea5c5bc44" />

3. For **Output Folder**, click on the folder icon, locate the tutorial folder, and click **OK**. 

4. Click **Run**. 

5. Once the export is complete, you should find the exported shapefile in your tutorial folder. Note that GIS recognizes a shapefile only when all its component files share the same name (e.g., .shp, .shx, .dbf). These files must be kept together in the same folder; otherwise, the shapefile may not open properly.
<p align="center"><img width="550"  alt="image41" src="https://github.com/user-attachments/assets/e5cf9d1a-0617-4fc1-b829-488e297f3c69" />

# Resources

ArcGIS Pro offers a wide range of tools for visualizing and analyzing geospatial data, and this tutorial only covers some of them. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

- [ArcGIS Pro Resources](https://www.esri.com/en-us/arcgis/products/arcgis-pro/resources) by Esri; 
- [ArcGIS Pro Introduction](https://guides.library.duke.edu/arcgispro) by Duke Library; 
- [ArcGIS Pro quick-start tutorials](https://pro.arcgis.com/en/pro-app/latest/get-started/pro-quickstart-tutorials.htm) by Esri; 
- [ArcGIS Pro Community](https://community.esri.com/t5/arcgis-pro/ct-p/arcgis-pro) for browsing resources, sharing knowledge, and connecting with other users. 

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei <siti.lei@dukekunshan.edu.cn> for further support.


















