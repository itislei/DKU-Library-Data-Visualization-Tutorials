# ArcGIS Online for Mapping Data and Spatial Analysis

_Siti Lei_

_Data and Visualization Librarian, Duke Kunshan University_

_Last updated: November 21, 2025_

This tutorial introduces how to create, visualize, analyze, and share data-driven interactive maps using ArcGIS Online.

[**Before we start 2**](#_pf1szgfkcsrm)

[Introduction 2](#_ftea6gtfe21v)

[About the tool 2](#_iformkkjbkjs)

[Datasets 2](#_soc0h8ux6lya)

[What is “spatial analysis” and “geoprocessing”? 2](#_xw7o3p1dxesg)

[**Part 1: Building Maps with Data 3**](#_klr5bjcfcb9)

[Sign in to ArcGIS Online 3](#_t4fdu5bc38rs)

[Create a New Map Project 3](#_taumatbea33a)

[Toolbars 3](#_wxae9lstzae5)

[Basemap 4](#_jj1c9ddcia7n)

[Add Data 5](#_dushbtoa5lfu)

[Structured Table Dataset 6](#_ox6dyat6ywx9)

[Geospatial Data File 10](#_ezmbiq7sp9ne)

[Acquire Data from ArcGIS Online 12](#_ulhwn1x4c8kn)

[Visualize Data 14](#_edl4yw28dbl5)

[Styles 14](#_m0809fsurzgw)

[Labels 15](#_9l3tqk53mqa8)

[Pop-ups 16](#_95nocggs7847)

[Save a Map 17](#_5edw5h1qkelg)

[Share a Map 19](#_vrfxn7osz7yy)

[Export Data 22](#_97tnb2a6hf68)

[**Part 2: Analyzing Data with Maps 25**](#_583s5r3yquvf)

[Tools 25](#_i4o4gi2x4454)

[Join Data 25](#_hfqak6724kyu)

[Find by Attributes and Locations 32](#_8dmskv28vi64)

[Find Closest 37](#_wgifpbzctw1h)

[Extract Data 44](#_srivbxkzb1k9)

[Model Builder 47](#_xu87dnleegnu)

[**Resources 57**](#_6ecg53nnrzmm)

# Before we start

## Introduction

In this tutorial, we will use China’s airport location dataset and provincial boundary dataset to explore the distribution of airports across provinces in China. DKU members may download the original dataset from CnOpenData through [DKU Only E-Resources](https://library.dukekunshan.edu.cn/academic-databases/) by following the instructions.

Tasks covered in this tutorial include:

1.  Changing the basemap
2.  Loading and displaying China’s provincial boundaries on a map
3.  Loading and displaying airport locations on a map
4.  Saving the project and exporting data as a shapefile

By the end of this tutorial, you will be able to use ArcGIS Online to create a provincial-level map of China showing the geographic distribution of airports.

## About the tool

ArcGIS Online will be used in the tutorial. Visit the [GIS guide](https://library.dukekunshan.edu.cn/geographic-information-system-gis/) for more information about the tool.

## Datasets

The sample datasets are derived from [CnOpenData](https://www.cnopendata.com/) and have been cleaned for the purpose of demonstration. Download the sample datasets below:

- [China Airport.csv](https://duke.box.com/shared/static/ycwqlrka3797epk9m0p3svmsocj8fj3c.csv)
- [China Province Boundary.zip](https://duke.box.com/s/7e2ksv0f7gw156wit9zjxw0stwxo59ws)

## What is “spatial analysis” and “geoprocessing”?

The second part of this tutorial introduces how to use geoprocessing tools to perform spatial analysis. To help ground these concepts, here is a brief overview:

**Spatial analysis** is the process of examining geographic data based on location, relationships, and patterns. It helps answer questions such as where features are located, how they are distributed, and how they interact with other geographic elements.

**Geoprocessing** refers to the set of operations used to manipulate, analyze, and manage geographic data. These operations include overlaying layers, buffering, clipping, dissolving, intersecting, and converting data formats. In GIS, geoprocessing tools help model spatial relationships, create new datasets from existing ones, and automate complex workflows.

# Part 1: Building Maps with Data

In Part 1, we will introduce the basics of ArcGIS Online, including how to import and load datasets, visualize your data on a map, and save or export your work.

## Sign in to ArcGIS Online

Follow the instructions in [Signing in to ArcGIS Online](https://library.dukekunshan.edu.cn/signing-in-to-arcgis/) to sign in to [ArcGIS Online](https://www.arcgis.com/index.html).

## Create a New Map Project

### Toolbars

1.  Once you successfully sign in to ArcGIS Online, you will see the view shown below. To start creating a map, go to the **Map** tab in the main menu — this opens a new map view where you can begin a new map project.

1.  The interface provides a variety of tools, organized in these toolbars:
2.  Contents toolbar
3.  Editing toolbar
4.  Viewing and Search toolbar

### Basemap

1.  The main map at the center serves as the basemap. By default, ArcGIS Online applies the “Topographic” map as the basemap.

1.  To select an alternative, navigate to the contents toolbar, select **Basemap**, and a list of available options will be displayed.

1.  Scroll down and select **Light Gray Canvas**.

1.  The reference system for China is not accurate. To correct this, we will create a new labeling system. First, close the current one by clicking the arrow to expand the details of the selected basemap.

1.  Then, click on the eye icon next to **Light Gray Reference** to hide it.

## Add Data

There are multiple ways to add data to a map project in ArcGIS Online - you can add datasets with location data, upload images, connect to external sources via URL, or create your own sketches directly in the map.

ArcGIS Online supports importing data from structured table formats such as comma-separated values files (.csv), Excel files (.xslx) with location fields (e.g., coordinates, addresses), and geospatial file formats including shapefile (.shp), GeoJSON, KML (.kml), and GeoPackage (.gpkg), and Geodatabase (.gdb).

### Structured Table Dataset

[China Airport.csv](https://duke.box.com/shared/static/ycwqlrka3797epk9m0p3svmsocj8fj3c.csv) is a data table containing information about every airport in China, including their names, addresses, coordinates, and year of construction. Let’s map this data on the map! Before we begin, make sure you have downloaded the file to your computer.

1.  Go to the contents toolbar, select **Add**, then **Add layer from file**.

1.  Click **Your device** button, then select **China Airport Dataset.csv** file (downloaded from the setup files) from its saved location and click **Open**. Alternatively, drag and drop the file into the pop-up window.

1.  Select **Create a hosted feature layer and add it to the map**, click **Next**.

1.  Confirm data type for each variable, and click **Next**.

1.  Click the arrow icon to expand the options, select **Latitude and longtitude**, click **Next**.

1.  Open the dropdown, then select **LAT** for the “Latitude” field and **LNG** for the “Longitude” field, click **Next**.

1.  Name the new layer as **China Airport Dataset**, then click **Create and add to map**.

1.  A map layer with all airport data points in China has been added to your map!

1.  Go to **Layers** in the contents toolbar to check the items that have been added to the project.

### Geospatial Data File

A shapefile is one of the most common geospatial data formats used in GIS, which stores geographic features (such as points, lines, or polygons) along with their associated attributes. Despite its name, a shapefile is actually a collection of several related files (e.g., .shp, .shx, .dbf) that must stay together for the data to function properly. ArcGIS Online can only read a shapefile directly from a zipped folder, which is why you should upload the .zip file without unzipping it.

[China Province Boundary.zip](https://duke.box.com/s/7e2ksv0f7gw156wit9zjxw0stwxo59ws) is a compressed folder containing a shapefile and its supporting files. It provides provincial-level boundary data for China, with each province represented as a polygon. Let’s add this data to the map! Before we begin, make sure you have downloaded the file to your computer, and **do not** unzip it.

1.  After download, go to the contents toolbar, select **Add** > **Add layer from file**.

1.  Select **Your device** option, then locate and click on the **China Province Boundaries.zip** file (downloaded from the setup files) from its saved location and click **Open**. Alternatively, drag and drop the file into the pop-up window. Click **Next** to continue.

1.  Make sure “Shapefile” is selected, then click **Next**.

1.  Name the new layer as **China Province Boundaries**, then click **Create and add to map**.

1.  It may take a moment to process. Once completed, a new layer named **China Province Boundaries** will appear in the **Layers** panel. Locate the **China Province Boundaries** layer, click the ellipsis (3-dot) icon next to it, and select **Zoom to layer**.

1.  This will automatically zoom to the area where your data is displayed on the map.

1.  Go back to the **Layers** panel, and click the eye icon to hide the **China Province Boundaries** layer for now.

### Acquire Data from ArcGIS Online

Not just a tool, ArcGIS Online is also a rich source of map data, with contributions shared by researchers worldwide. For example, to understand where airports are located within provinces, we need to add a China province layer to the map, which can be directly imported from the ArcGIS Online database.

1.  Go to the contents toolbar, then **Add**, **Browse layers.**

1.  Switch the source from **My content** to **ArcGIS Online**.

1.  Type in the keyword “China province” and press **Enter** on your keyboard.

1.  Locate the item **China Province Boundaries** by Esri in the search results, click **\+ Add**.

1.  Use the **Zoom In/Out** tool under the viewing and search toolbar to examine the data in detail.

1.  Click **Remove** to delete the layer from your map.

## Visualize Data

### Styles

1.  To customize the appearance of data points, lines, or polygons on the map, first make sure that you have selected the target layer under **Layers**. A blue strip will appear on the left of the selected layer’s title.

1.  Then, select **Styles** under the editing toolbar and use the settings to adjust the appearance of the data points according to your preference. For best practices in selecting colors or patterns for geospatial data and maps, refer to the [Select Visualization Elements](https://library.dukekunshan.edu.cn/data-visualization/#:~:text=4.%20Select%20Visualization%20Elements) section in the [Data Visualization guide](https://library.dukekunshan.edu.cn/data-visualization/). Click **Done** when the edits are complete.

### Labels

1.  You can configure labels for a map layer. To do so, first, make sure that you have selected the target layer under **Layers**. A blue strip will appear on the left of the selected layer’s title.

1.  Next, select **Labels** under the editing toolbar to start editing. Make sure you toggle on **Enable labels** and select **Name** field as the **Label field** to show the name of each province (since we turned them off in the basemap). You can also adjust the settings to customize their look.

### Pop-ups

1.  Click on a random data point on the map — this will trigger a pop-up displaying all associated information for that specific point.

1.  To configure the pop-ups or edit the displayed information in the pop-up, first make sure that you have selected the target layer under **Layers**. A blue strip will appear on the left of the selected layer’s title.

1.  Next, go to **Pop-ups** under the editing toolbar to customize the content displayed.

## Save a Map

ArcGIS Online does **not** save your map project automatically, so be sure to manually save it each time before quitting the page.

1.  To save a new-created map project, go to the contents toolbar, click **Save and open**, then **Save as**.

1.  Name the project as **China Airport Map Project**, add other details if needed, and click **Save**.

1.  Click the hamburger (3-line) icon in the top left corner, then select **Content** - this is where your saved work will be stored. You can also find it under the main menu.

1.  Every time before quitting the project, go to the contents toolbar, click **Save and open**, then click **Save** to apply your changes.

## Share a Map

One advantage of using ArcGIS Online is that it allows easy sharing of map projects. With an institutional license, DKU members can share their projects with Duke and DKU users, make them public, or keep them private for self-view only.

You can also set up a group to make your project or items visible or editable to group members. Follow the instructions [here](https://doc.arcgis.com/en/arcgis-online/share-maps/create-groups.htm) to create a group. If you have any questions, please contact the Data and Visualization Librarian ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)).

1.  Go to **Content**, then **My content**. Locate the item you want to share, and click on its title.

1.  Alternatively, click on the ellipsis (3-dot) icon next to the item and select **View details**.

1.  From the right-hand pane, click **Share** to open the sharing options.

1.  Choose **Everyone (public)** under sharing options, and click **Save**.

1.  Click **Review sharing** to check the items whose sharing permissions will be updated accordingly.

1.  Click **Update sharing** to confirm the changes.

1.  Now, your map should be visible by the public.

## Export Data

For each layer created or added to a map project, you can export it as a shapefile to open in other GIS software or store on your local computer. In this tutorial, we will use the airport layer as an example.

1.  Go to **Content**, then **My content**. Make sure the item you select is of the “Feature layer (hosted)” type - otherwise, it will not support shapefile export.

1.  Click on the ellipsis (3-dot) icon next to the item title, select **View details**. You can also do it by clicking on the item title.

1.  Under the **Overview** tab, click **Export data** from the right pane.

1.  Then, select **Export to shapefile** from the dropdown menu.

1.  Name the new file as **China Airport Dataset**, add other details if needed, and click **Export**.

1.  Once the export is complete, a new page will appear showing the file type as “Shapefile”. You can also find it under the **Content** tab.

1.  Click **Download** on the right pane to save the file in your local computer.

# Part 2: Analyzing Data with Maps

In Part 2, we will use some geoprocessing tools in ArcGIS Online to gain insights from China’s airport and province boundary datasets. By the end, you will be able to use maps to answer these questions:

1.  How are airports distributed across the provinces of the country? Which provinces have higher or lower densities of airports?
2.  How many airports are there in Jiangsu province? What are these airports, and where are they located?
3.  Which 3 airports in Jiangsu province are closest to DKU campus?
4.  How to export the layer into a format that is shareable and downloadable (e.g., Shapefile, CSV)?
5.  Which provinces have more than 10 airports?

## Tools

### Join Data

The first question “How are airports distributed across the provinces of the country? Which provinces have higher or lower densities of airports?” focuses on the distribution and density of airport locations across the country.

Since the two datasets we need to answer this question are currently separate, we need to merge them into a single layer. Many of the geoprocessing tools can achieve this (like **Aggregate Points**), but the tool that will be introduced in this tutorial is **Join Features**.

1.  Go to the Editing toolbar, click on **Analysis**.

1.  Select **Tools**. Alternatively, click the tool icon in the header menu.

1.  Under **Summarize data**, select **Join Features**.

1.  Now, let’s configure our input and output. First, for the **Target layer**, select **China Province Boundaries** layer from the dropdown.

1.  For the **Join layer**, select **China Airport Dataset** layer from the dropdown.

1.  Under the **Join settings**, toggle on **Use spatial relationship**.

1.  For the **Spatial relationship**, select **Completely contains** from the dropdown menu.

1.  For the **Join operation**, select **Join one to one** from the dropdown menu.

1.  Since we are analyzing the density of airports across provinces, we first need to calculate the number of airports in each province. Under the **Multiple matching records**, select **Calculate count only**.

1.  For the **Join type**, make sure **Inner join** is highlighted.

1.  Under the **Result layer**, give a name to the new layer in the **Output name** field, and select the designated folder to save the output. Note that the name should be unique across the organization no matter where you save the layer. Example: **Count of Airports in Provinces_\[Your NetID\]**.

1.  Click **Run** to start processing.

1.  To check the progress, click on the history icon in the header menu.

1.  Once the analysis is completed successfully, a new layer named **Count of airports in provinces** will appear in the **Layers** and the map. Let’s focus on this layer by hiding the other two layers and keep only the newly created one visible.

1.  The new layer called **Count of airports in provinces** will show up in the **Layers** pane. When you click on a province polygon, the pop-up will display a new attribute called **Join_Count**, followed by the total number of airports in the corresponding province.

1.  Click the ellipsis (3-dot) icon next to **Count of airports in provinces** layer and select **Show table**.

1.  The data table attached to this layer will appear with two new attributes named **Join_Count** and **Admin Name**. **Join_Count** indicates the number of airports in each corresponding province, **Admin Name** represents the administrative region used in the spatial analysis.

### Find by Attributes and Locations

Let’s move to the second question: What and where are the airports in Jiangsu Province?

To answer this, we can use the **Find by Attributes and Location** tool. This tool allows us to set specific query conditions (such as filtering by province name) to automatically extract only the airports that meet our criteria. Once applied, it will generate a subset of the data showing all airports located within Jiangsu.

1.  Go to the Editing toolbar, click on **Analysis**.

1.  Select **Tools**. Alternatively, click the tool icon in the header menu.

1.  Under the **Find locations**, select **Find by Attributes and Location**.

1.  Click on **\+ Build new query** under **Criteria**.

1.  For **Find features from**, select **China Airport Dataset** layer from the dropdown, then select **Attribute expression**, click **Next**.

1.  For **Where** fields, we will define the criteria. First, choose **All of the following are true**. Then, set **Province_EN** as the field, select **equal** as the operator, and select or enter **Jiangsu** as the value. Once the condition is set, click **Add** to apply it.

1.  Under the **Result layer**, give the new item a name in the **Output name** field, and select the designated folder to save the output. Note that the name should be unique across the organization no matter where you save the layer. Example: Airports in Jiangsu_\[Your NetID\].

1.  Click **Run** to start processing.

1.  To check the progress, click on the history icon in the header menu.

1.  Once the analysis is completed successfully, a new layer named **Airports in Jiangsu** will appear in the **Layers** and the map. Let’s focus on this layer by hiding the other layers and keep only the newly created one visible.

1.  The map will update to show the new layer we just created, automatically zooming into Jiangsu province.

1.  Click the ellipsis (3-dot) icon next to **Airports in Jiangsu** layer and select **Show table**.

1.  There should be 11 records in the table, meaning that there are 11 airports in Jiangsu province.

### Find Closest

The third question we want to solve is: what are the 3 closest airports to DKU. To do that, we will first create a new layer with DKU campus’s location data.

1.  Click on the **Search** tool in the Searching and Viewing toolbar.

1.  Click **Use current location**, Or, enter **Kunshan, Jiangsu**, and select the first option from the dropdown. This will locate you to the Kunshan region on the map. Then, navigate to the Duke Kunshan University.

1.  Go to **Add**, then select **Create sketch layer**.

1.  Under the **Point feature** in the **Sketch** pane, name the new data point as **DKU**.

1.  Make sure the stamp icon is selected in the sketch toolbar, and click on two random places in the campus area on the map.

1.  We only need one data point actually, so let’s delete one of them. To do so, click **Select** (cursor icon) from the sketch toolbar. Then click on the point you want to delete, and click on **Delete** or hit **Backspace** on the keyboard.

1.  Go to **Layers**, rename the sketch layer as **DKU campus**, and click **OK**.

1.  Next, go to **Analysis**, select **Find Closest** under the **Use proximity**.

1.  Select **DKU campus (Points)** as input layer, and **Airports in Jiangsu layer** as near layer.

1.  For the **Analysis settings**, toggle on **Limit the number of closest locations**, and enter **3** as the max number of input. Make sure **Limited the search range** is toggled off.

1.  Under the **Result layer**, give a name to the new layer in the **Output name** field, and select the designated folder to save the output. Note that the name should be unique across the organization no matter where you save the layer. Example: Closest airports to DKU_\[Your NetID\].

1.  Click **Run** to start processing.

1.  To check the progress, click on the history icon in the header menu.

1.  Once the analysis is completed successfully, a new layer set named **Closest airports to DKU** will appear in the **Layers** and the map. Let’s keep the rest of the layers invisible.

1.  Click on the arrow icon next to **Closest airports to DKU** layer set, click on the ellipsis (3-dot) icon next to **Connecting Lines** and select **Show table**.

1.  The data table should display 3 records, along with two new attributes - **Near Rank** and **FindExistingLocation** - which indicate the airport names and their rankings by distance.

### Extract Data

Lastly, the analysis tools allow exporting layers in CSV, file geodatabase, shapefile, and KML. Let’s say we want to export the data table attached to our closest airports to the DKU layer in a table csv format. We already know how to view the data table in the map view, but how to download that in a csv format?

1.  Go to the Editing toolbar, click on **Analysis**.

1.  Select **Tools**. Alternatively, click the tool icon in the header menu.

1.  Under **Manage Data**, select **Extra Data**.

1.  For **Input layers**, select **Closest airport to DKU - Nearest Features** and **Closest airport to DKU - Connecting Lines**.

1.  Under **Result layer,** select CSV as the output data format, name the new output as **Top 3 closest airports**, and select the designated folder to save the output.

1.  Click **Run** to start processing.

1.  Click on the history icon in the header menu to check the progress. Then, click on the ellipsis (3-dot) icon next to the processing record, and click **View details**.

1.  Click on the ellipsis (3-dot) icon next to **Top 3 closest airports**, then **Open item details**.

1.  A new item page will open. Click on the **Download** button in the right pane to download and save the file in your local computer.

1.  Open the **Nearest_Features** file in Excel to view the ranked list of airports closest to the DKU campus. Note that Chinese text may not always export correctly.

## Model Builder

While we just demonstrated how to answer multiple questions by running different analysis tools step by step, there is a way to streamline the entire process without executing each tool manually - that’s **Model Builder**.

With **Model Builder**, instead of running each tool manually, you can build a workflow where outputs from one step feed directly into the next. This is especially useful when working with large datasets, performing multi-step analyses, or repeating the same workflow with different inputs.

In this demo, we will answer this question: which provinces in China have more than 10 airports?

1.  Return to the map project view. If you can’t find it, go to the ArcGIS Online homepage and navigate to **Content** \> **My content**. Open the **Airport within province** web map item.

1.  Click on **Analysis**.

1.  Select **ModelBuilder**. Alternatively, click the Model Builder icon in the header menu.

1.  Click **Connect** to continue.

1.  Make sure the **Disconnect** button is showing up, then click **Create model**.

1.  For the model, let’s call it **Provinces with over 10 airports**, then click **Save**.

1.  In the new window, click on the **Add tools** icon.

1.  Select 2 tools: **Join Features** and **Filter by Attributes**, then click **Add**.

1.  The tools will be added to the canvas and displayed in grey. Double-click on the **Join Features** box.

1.  In the pop-up, select **China Province Boundaries** as the target layer, and **China Airport Dataset** as the join layer.

1.  Next, toggle on **Use spatial relationship** and select **Completely contains**. For the **Join operation**, choose **Join one to one**, and ensure that **Calculate count only** under the **Multiple matching records** option is selected.

1.  For **Join type**, select **Inner join**. For the **Result type**, select **Create intermediate data** from the dropdown - this means the output from this analysis tool will not be saved as a permanent layer. Click **Confirm**.

1.  Now, the canvas should show two additional items in blue, representing the datasets we just configured. In addition, the tool box appears in yellow, and the output box appears in green.

1.  Next, double-click on **Filter by Attributes**.

1.  For the **Input dataset**, select **Join result**.

1.  Click on **\+ Build new query**.

1.  Select **Expression** and click **Next**.

1.  For **Where** fields, choose **All of the following are true** first. Then, set **Join Count** as the field, select **is greater than** as the operator, and select or enter **10** as the value. Once the condition is set, click **Add** to apply it.

1.  For the result layer, make sure the **Create hosted layer** is selected under the **Result type**, then give a name to the new layer in the **Output name** field. Note that the name should be unique across the organization no matter where you save the layer. Example: Chinese provinces with over 10 airports_\[Your NetID\].

1.  In the canvas, all items are now connected in a workflow with arrows and color-coded accordingly. Click **Run** to execute the model.

1.  Once the model runs successfully, a green check mark will appear on both the tool and output boxes.

1.  In the **Layers** pane, a new layer called **Chinese provinces with over 10 airports** will now appear.

1.  Click the **Save** icon, then close the tab.

1.  Under **Models in this map**, you will find the model we just saved. Click on +its name to reopen it. You can swap in different datasets and run it again anytime to repeat the same analysis.

1.  Remember to save the project manually.

# Resources

ArcGIS Online offers a wide range of tools for visualizing and analyzing geospatial data, and this tutorial only covers some of them. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

- [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;
- [Perform analysis in Map Viewer](https://learn.arcgis.com/en/paths/data-analysis/) by Esri;
- ArcGIS Online [Tool Documentation](https://doc.arcgis.com/en/arcgis-online/analyze/aggregate-points-mv.htm)
- [ArcGIS Online Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online) for browsing resources, sharing knowledge, and connecting with other users.

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.