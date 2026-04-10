# **Creating Temporal Maps with Time Slider**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: 2026*

This tutorial introduces how to create time-based interactive maps using temporal data in ArcGIS Online.

[**Before we start	1**](#before-we-start)

[Introduction	1](#introduction)

[About the tool	1](#about-the-tool)

[Datasets	2](#datasets)

[Sign in to ArcGIS Online	2](#heading=h.t4fdu5bc38rs)

[Import Temporal Data	2](#import-temporal-data)

[Customize Basemap	6](#customize-basemap)

[Visualize Event Data	6](#visualize-event-data)

[Configure Time Setting	7](#configure-time-setting)

[Configure Time Slider	8](#configure-time-slider)

[**Resources	8**](#resources)

# 

# **Before we start** 

## **Introduction** 

This tutorial uses a subset of social events to examine how they spread throughout North America over time.

Tasks covered in this tutorial include:

1. Importing temporal data  
2. Loading and displaying event locations on a map  
3. Configuring time setting  
4. Adjusting animation settings (time range, speed, and playback)

By the end of this tutorial, you will be able to use ArcGIS Online to create an animated map of North America that shows the geographic distribution of events related to the Black Lives Matter movement.

## **About the tool** 

ArcGIS Online will be used in the tutorial. Visit the [GIS guide](https://library.dukekunshan.edu.cn/geographic-information-system-gis/) for more information about the tool.

## **Datasets** 

The sample dataset is sourced from news articles and Wikipedia and has been cleaned for demonstration purposes. Download the sample dataset below:

* BLM\_events.xlsx (Sources are listed under **REFERENCE** column)

## **Import Temporal Data** 

BLM\_events.xlsx is a data table containing information about a selection of social events related to the Black Lives Matter movement, including event names, regions, coordinates, start and end dates, event type, and exposed population. Let's map this data. Before we begin, make sure you have downloaded the file to your computer.

1. Sign in to [ArcGIS Online](https://www.arcgis.com/index.html). If you are a first time user, follow the instructions in [Signing in to ArcGIS Online](https://library.dukekunshan.edu.cn/signing-in-to-arcgis/).

2. Go to **Map** in the header menu.  
3. Once in the map view, go to the left contents toolbar, select **Add**, then **Add layer from file**.

![][image1]

4. Click **Your device** button, then select **BLM\_events.xlsx** file (downloaded from the setup files) from its saved location and click **Open**. Alternatively, drag and drop the file into the pop-up window.

**![][image2]**

5. If you have multiple worksheets in the file, select the one that’s going to be used in this project. If you are using BLM\_events.xlsx dataset, make sure **Example** is selected.

**![][image3]**

6. Confirm the data type for each variable. Since we are creating a time series map, ensure that the date variables (**DAY\_START** and **DAY\_END**) are set to the **Date** type. In this sample dataset, also verify that **LATITUDE** and **LONGITUDE** are set to **Single** (or **Double**) and that **POPULATION\_EXPOSURE** is set to **Integer**. Click **Next** when ready.

**![][image4]**

7. Confirm the location data field again, then click **Next**.

**![][image5]**

8. Name this dataset and select the designated folder to save it. Note that the name should be unique across the organization no matter where you save the data. Example: **BLM\_events\_\[Your NetID\]**. Click **Create and add to map**.

![][image6]

9. A map layer with all data points in the dataset will be added to your map\!

![][image7]

10. Go to **Layers** in the contents toolbar to check the data layer added to the project.

![][image8]

## **Customize Basemap** {#customize-basemap}

1. In the map view, go to **Basemap** in the contents toolbar.

![][image9]

2. Choose **Dark Grey Canvas**.

![][image10]

3. Click the **close icon** to close the options.

![][image11]

4. Go to **Save and open** \> **Save as**.

![][image12]

5. Name this map project and select the designated folder to save it. Note that the name should be unique across the organization no matter where you save the project. Example: **Time\_Series\_Map\_\[Your NetID\]**. Click **Save**.

![][image13]

## **Visualize Event Data** 

Since our dataset contains population exposure and event type, let's color-code the points using this data: different colors represent different event types, while the symbol size represents the population exposure count.

1. Make sure the **BLM\_events** layer is selected under **Layers**, then open **Styles** from the right editing toolbar. 

![][image14]

2. For **Choose attributes**, click **\+ Field**. 

![][image15]

3. Select **EVENT\_TYPE** and **POPULATION\_EXPOSURE** from the menu, then click **Add**.

![][image16]

4. Under Pick a style, choose **Types and size**. You can click the **Styles option** button to further customize the visual elements.

![][image17]

## **Configure Time Setting** 

Time settings can be configured in the detail view of each map item. To access them, first return to your content.

1. Make sure the map project has been saved, then click the **hamburger (three dashes)icon** in the top-left corner of the page and select **Content**.

**![][image18]**

2. Locate the BLM\_events map layer, click on the ellipsis (three-dot) icon and go **View details**.

![][image19]

3. In the layer page, scroll down to **Layers** and click **Example** to expand the item.

![][image20]

4. In the item page, scroll down to **Time settings**, then click **Edit**.

![][image21]

5. In the pop up, check **Enable time**. Next, check **time ranges with a start and end time**, and make sure the variables (DAY\_START and DAY\_END) are picked up correctly. Click **OK** to confirm.

![][image22]

6. Return to **Content**, click to open the **Time Series Map** project again.  
7. In the detail page, select **Open in Map Viewer**. 

![][image23]

8. Now, a time slider will appear in the map.

![][image24]

## **Configure Time Slider** 

In ArcGIS Online, you may configure the time range, speed, and playback for your temporal data. 

1. Once the time setting has been configured successfully and the time slider appears in the map view, click the settings icon on the right side of the slider. 

![][image25]

2. In the pop-up window, explore each tab to adjust how the animation works. For example, to make the animation play faster, go to **Playback rate** and drag the slider all the way to the right to "Fast."

![][image26]

3. Make sure you save the project before leaving the page by going to **Save and open \> Save** in the left content toolbar.

![][image27]

# **Resources** 

ArcGIS Online offers a wide range of tools for visualizing and analyzing geospatial data, and this tutorial only covers some of them. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

* [Configure time settings](https://doc.arcgis.com/en/arcgis-online/create-maps/configure-time-mv.htm) by Esri for different map items and their respective time properties;  
* [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;  
* ArcGIS Online [Tool Documentation](https://doc.arcgis.com/en/arcgis-online/analyze/aggregate-points-mv.htm)  
* [ArcGIS Online Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online) for browsing resources, sharing knowledge, and connecting with other users.

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.
