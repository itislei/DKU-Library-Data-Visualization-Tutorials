# **Storytelling with ArcGIS StoryMaps**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: March 3, 2026*

This tutorial introduces how to create map-based digital stories with ArcGIS StoryMaps.

# **Before we start**

## **Introduction**

In this tutorial, we will create a map-based digital story that explores airport data across China, building upon the spatial analysis conducted in ArcGIS Online. This demonstration StoryMap transforms spatial data into a clearer picture of national connectivity, presenting the analysis through a structured and engaging narrative format.

Because this tutorial uses the web map and layers developed in the [ArcGIS Online tutorial](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/ArcGIS%20Online/ArcGIS%20Online%20for%20Mapping%20Data%20and%20Spatial%20Analysis.md), it is recommended that you complete the ArcGIS Online tutorial before proceeding.

By the end of this tutorial, you will be able to use ArcGIS StoryMaps to design a digital narrative, [Mapping of China’s Airports](https://storymaps.arcgis.com/stories/bde557a48c40485f945327a1ea78c4db), that visualizes geographic distribution and communicates key analytical findings effectively.

## **About the tool**

ArcGIS StoryMaps will be used in the tutorial. Visit the [tool overview](https://www.esri.com/en-us/arcgis/products/arcgis-storymaps/overview) for more information.

## **Dataset**

[ArcGIS Online Demo](https://arcg.is/TqDLG1) (web map) \- Layers from this web map will be used in this tutorial.

Additionally, download the [Sample Dataset.zip](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/ArcGIS%20StoryMaps/Sample%20Dataset.zip) file to your local computer. Unzip it and you can find the folder contains the following files:

* **sites** (folder of images)  
* **Captions.docx** (text captions will be used in this tutorial)  
* **Map\_tour\_data.csv** (table exported from the [ArcGIS Online Demo](https://arcg.is/TqDLG1) web map)

# **Navigate to ArcGIS StoryMaps**

1. Sign in to [ArcGIS Online](https://www.arcgis.com/index.html) institutional account. If you are a first time user, follow the instructions in [Signing in to ArcGIS Online](https://library.dukekunshan.edu.cn/signing-in-to-arcgis/).  
2. On the main page, click on the 9-dot (waffle) icon in the upper corner.

![][image1]

3. This will open the menu displaying all add-on products available under our institutional license. From the list, select **StoryMaps**.

![][image2]

4. Now, you will be directed to ArcGIS StoryMaps.

# **Create a StoryMap**

1. Once you are in the ArcGIS StoryMaps, click on the **\+ Create** button on the upper right corner. Select **Story** from the dropdown list. You will be directed to a new page where you can begin adding and editing content.

![][image3]

2. In the new page, first, enter the story title by copying and pasting the content under \#1 in captions.docx into the title field.  
3. Copy and paste the content under \#2 into the StoryMap as the subtitle.

![][image4]

4. You may click on the **Change panel appearance** icon to adjust the alignment.

![][image5]

5. Next, click the **Add cover image or video** button in the upper right corner. 

![][image6]

6. In the pop-up window, click **Browse your files**.

![][image7]

7. Navigate to the folder where the site images are stored, select **01\_Airplane\_on\_the\_Runway.jpg**, and click **Open**. 

![][image8]

8. Then click **Add**.

![][image9]

9. You can adjust the image by clicking the **Options** (Settings) icon, or replace or delete it using the **More actions** (three-dot/ellipsis) icon.

![][image10]

10. ArcGIS StoryMaps includes a variety of pre-made design themes that can be applied directly to your project. For example, click **Design** in the header to explore these options.

![][image11]

11. The **Design** pane will open, allowing you to customize the appearance of your StoryMap using predefined themes and style elements. In this tutorial, we will use a specific design as an example, but you are welcome to choose the theme that best fits your preference.

![][image12]

12. In this project, change the cover layout to **Side-by-side** and toggle on **Navigation**. We will configure the navigation menu later in the tutorial.

![][image13]

13. For the theme, select **Ridgeline**. You can explore additional options by clicking **Featured themes gallery**.

![][image14]

14. Once you have made your selections, close the **Design** pane.  
15. The cover has now been set up. Note that your changes are saved automatically.

![][image15]

# **Text Content**

1. Scroll below the cover to the blank area, click the **\+** button, and select **Text**.

![][image16]

2. Copy and paste the content under \#1 in captions.docx into the text box. Note that text separated by blank lines will automatically be divided into individual text blocks.

![][image17]

3. Triple click to highlight **“About the Project”**, then switch the font from **Paragraph** to **Heading 1**.

![][image18]

4. **“About the Project”** is now formatted as a larger, bold heading. It also appears in the navigation menu for easier access.

![][image19]

5. Next, select the quote below “About the Project”, then switch the font from **Paragraph** to **Quote**.

![][image20]

6. Copy and paste the content from section \#2 in captions.docx into the quote source box, then click outside the box to save your changes. Leave the last paragraph in this section as the default text.

![][image21]

# **Table**

1. Below the content added so far, click the **\+** icon to insert one **separator** and one text asset. Then copy and paste the content from section \#3 in captions.docx into the text box.

![][image22]

2. For **“Map 1”,** switch the font from **Paragraph** to **Heading 1**, and for **“Provinces with More Than 10 Airports”**, switch the font from **Paragraph** to **Heading 2**.

![][image23]

3. Below the text, click the \+ icon and select Table from the list.

![][image24]

4. Copy and paste the table values from section \#4 in captions.docx into the table. Note that importing data from an existing file is not supported, and you cannot paste all content at once. You will need to copy and paste the content into each cell individually.  
5. If you need additional rows or columns, hover along the table edges and click the three-dot (ellipsis) icon. Then select **Insert row below** to add them.

![][image25]

6. Lastly, after entering all the data into the table, add a caption below the table using the content from section \#5 in captions.docx.

![][image26]

# **Charts**

1. Continue the Map 1 section, click on the **\+** icon and select **Chart** from the list.

![][image27]

2. Select **Bar chart** from the options and click **Done**.

![][image28]

3. In the left pane of the new page, copy and paste the content from section \#6 in captions.docx into the table. Note that importing data from an existing file is not supported, and you cannot paste all content at once. You will need to enter the content into each cell individually. Adding multiple columns of data is supported.

![][image29]

4. Switch to **Settings** from **Data** tab, copy and paste 

![][image30]

5. Remove the values under **Chart title**, enter **Region of China** in the **Category axis title** field, and **Count of Provinces** in the **Value axis title** field.

![][image31]

6. Toggle on **Customize axis**, and enter **3** in the field.

![][image32]

7. Review the changes and click **Save** to confirm.

![][image33]

8. Back to the project, click **Add another block** as we are going to add the donut chart.

![][image34]

9. Select **Donut chart** from the options and click **Done**.

![][image35]

10. Again, copy and paste the content under \#6 in captions.docx into the table on the left pane of the new page. Note that the donut chart can only work with two data columns.

![][image36]

11. Switch to the **Settings** tab and delete all content in the **Chart title** field.

![][image37]

12. Review the chart, then click **Save** when it's ready.

![][image38]

13. Return to the project, then copy the content from section \#7 in captions.docx and paste it under the charts as the caption. Click anywhere outside the box to save the changes. 

![][image39]

14. You may add another chart by clicking the **Add another block** icon, but note that a maximum of three charts is allowed per row.

![][image40]

# **Web Map**

1. Below the charts, click on the **\+** icon and select **Map** from the list.

![][image41]

2. On the new page, if you followed and completed the ArcGIS Online tutorial, you should be able to find your web map project saved under **My Content**. Click on it to continue.

**![][image42]**

3. If you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly.

![][image43]

4. Under **Layers** tab, make sure that **Count of airports in provinces** and **China Province Boundaries** layers are visible as all others are hidden.  
5. Under **Layers** tab, make sure that **Chinese provinces with other 10 airports** and **China Province Boundaries** layers are visible as all others are hidden.

![][image44]

6. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level, then click **Save** to continue.

![][image45]

7. Back to the project, copy the content from section \#8 in captions.docx and paste it under the map as the caption.

![][image46]

8. Hover over the map, and a toolbar will appear. From there, you can edit the map view, adjust the view window, or remove the map.

![][image47]

9. In the next line, click **\+** icon to add a new separator.

![][image48]

# **Sidecar**

1. Below the web map, click on the **\+** icon and select **Text** from the list.  
2. Copy and paste the content under \#9 in captions.docx into the text box. Change the font style of **“Map 2”** from Paragraph to **Heading 1**, and **“Airport Counts Across All Provinces”** to **Heading 2**.

![][image49]

3. Below the text box, click on the **\+** icon and select **Sidecar** from the list.

![][image50]

4. From the options, select **Floating** and click **Save**.

![][image51]

5. Under the navigation, click on **\+ Add** button.

**![][image52]**

6. Select **Map** from the options.

![][image53]

7. On the new page, if you followed and completed the ArcGIS Online tutorial, you should be able to find your web map project saved under **My Content**. Click on it to continue. If you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly.

**![][image42]**

8. Under **Layers** tab, make sure that **Count of airports in provinces** and **China Province Boundaries** layers are visible as all others are hidden.

![][image54]

9. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level, then click **Save** to continue.

![][image55]

10. You may use the floating toolbar to adjust the map view.

![][image56]

11. Copy and paste content under \#10 in captions.docx to the left text box.

![][image57]

12. You may adjust the look of the text. For example, make“higher counts” and “larger and darker” a bold and darker color, while making “fewer airports” and “smaller and lighter” a brighter color.

![][image58]

13. Click on the **\+** icon at the bottom right. We are going to add another slide here.

![][image59]

14. Click on **\+ Add** button and select **Map** from the options. On the new page, open the ArcGIS Online tutorial project either created by yourself under **My Content**, or the one under **My Organization** created by the instructor (if you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly).   
15. Note that there are two dots that are the smallest and brightest on the map. First, zoom in on the top one.

![][image60]

16. Make sure the dot is in the center, then click **Save** to continue.    

![][image61]

17. Copy and paste content under \# 11in captions.docx to the left text box.

![][image62]

18. Repeat the same step and add another slide with the other white dot at the bottom map, along with the corresponding content under \#12 in captions.docx.

![][image63]

19. Scroll down to the sidecar section below and add a **separator** to continue.

# **Swipe**

1. Below the web map, click the **\+** icon and select **Text** from the list. Copy and paste the content under \#13 in captions.docx into the text box. Then change the font style of **“Map 3”** from **Paragraph** to **Heading 1**, and change **“Airport Locations in Jiangsu Province”** to **Heading 2**.  
2. Below the text, click the **\+** icon and select **Swipe**.

![][image64]

3. First, click on **Add media** on the left pane.

**![][image65]**

4. Select **Web Map** from the options. Note that you can also add an image (e.g., scan of physical map) here.

**![][image66]**

5. On the new page, again, select the ArcGIS Online tutorial project either created by yourself under **My Content**, or the one under **My Organization** created by the instructor (if you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly).   
6. Under **Layers** tab, make sure that **Airports in Jiangsu** and **China Province Boundaries** layers are visible as all others are hidden.

![][image67]

7. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level. Make sure Jiangsu Province is centered and clearly visible on the view, then click **Save** to continue.

![][image68]

8. Click on **Add web map** at the right pane.

![][image69]

9. Now, filter to **Living Atlas** and **World**, then pick an option from the result list. For this tutorial, let’s pick up **Open Basemap (Streets)**.

![][image70]

10. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level. Make sure Jiangsu Province is centered and clearly visible on the view, then click **Save** to continue.

**![][image71]**

11. If you think the visibility level needs changes, you can always click on the **Edit** icon under each map in the swipe to change it.

**![][image72]**

12. Once you have finished editing the map, drag the **Swipe** icon across the map to compare the layers. You can also use the **Zoom In** and **Zoom Out** icons to adjust the visibility level.

![][image73]

13. Don’t forget to add a caption to the maps. Copy and paste the content under \#14 in the caption file.

**![][image74]**

14. Lastly, hover over the edges of the map and click **Medium** in the floating toolbar. This will enlarge the map view.

![][image75]

15. In the new section below, add a **separator** to continue.

# **Map Tour**

1. Below the swipe, click the **\+** icon and select **Text** from the list. Copy and paste the content under \#15 in captions.docx into the text box. Then change the font style of **“Map 4”** from **Paragraph** to **Heading 1**, and change **“Three Closest Airports to DKU”** to **Heading 2**.  
2. Below the text, click the \+ icon and select **Map tour**.

**![][image76]**

3. From the options, select **Upload photos**.

![][image77]

4. Click **Browse your files**.

![][image78]

5. Navigate to the sites folder from the sample datasets, and select all image files except 0\_Airport\_on\_Runway, then click **Open**. To select multiple files at once, click the first item, press the **Shift** key on your keyboard, and then click the last item to select all at once.

![][image79]

6. Make sure 4 images are selected, click **Add**.

![][image80]

7. For the layout, select **List** under **Explorer tour**, and click **Save**.

![][image81]\+

8. Copy and paste the content under \#16 in captions.docx as the title and \#17 as the description for the first image into the text box.

![][image82]

9. Next, open **Map\_tour\_data.csv** on your local computer. Drag and select the values under **LAT** and **LNG** for **Duke Kunshan University**.

 ![][image83]

10. Right-click and select **Copy**. Alternatively, press **Ctrl \+ C** on Windows (or **Command \+ C** on Mac) to copy.

![][image84]

11. Go back to the StoryMap and click **Add location** on the **Duke Kunshan University** card.

![][image85]

12. On the new page, paste the values into the search box in the top-right corner. A dropdown list of matching place names will appear. However, since we are searching by coordinates, press **Enter** to commit the search.

![][image86]

13. This will take you to a location near the DKU campus. Zoom out slightly and you will notice the marker is a bit off. Click **Close**, then reselect the correct location. If you are satisfied with the updated location, click **Add to map** to confirm.

![][image87]

14. Move your cursor to the center of DKU and click to place a marker.

![][image88]

15. Set the visibility level to **Use the current zoom level**, then click **Save**.

![][image89]

16. Once editing is complete, switch to the second image from the bottom of the list, or use the mouse wheel to continue making changes.  
17. Repeat steps (\#8–15) to complete the information for the remaining three images.  
18. Then scroll down to the map tour section below and add a **separator** to continue.

# **Credits**

1. In the blank area, create a new text box and copy and paste the content under \#24 in captions.docx into the text box. Change the font style to **Heading 1**.  
2. Then create another text box below. Copy and paste the image source titles under \#25 in captions.docx into this text box.  
3. Select each line of text, click **Link**, and hyperlink the titles using the corresponding URLs listed under \#26 in captions.docx.

![][image90]

4. Scroll down to the bottom of the page, and add your self author credits. 

![][image91]

# **Publish the StoryMap**

1. Once completed the editing, Go to the top menu and click **Publish**.

![][image92]

2. You may change the title, subtitle, cover by clicking on the **Edit** on the left pane.

![][image93]

3. On the right pane, set the sharing level to **Organization**.

![][image94]

4. If you have a group or collaborating with others, you may set the **group sharing**.

![][image95]

5. You may also set some advanced options for the sharing, such as allowing others to duplicate or showing your project in the web search results if you set the project to be visible to the public.  
6. When everything is set, click **Publish**.

![][image96]

7. Now the project should be published. And there are several ways to share it to others and view.

![][image97]

# **View and Save StoryMap**

1. After the project is completed, you may click on the View published story button, or copy the link and open in a new tab, or scan the QR code to open. You may also share the link or the QR code.

![][image98]

2. You can always find the projects or drafts in your [StoryMaps content](https://storymaps.arcgis.com/content).   
3. In the project, you may use the mouse wheel and cursor to scroll through and review the content.  
4. Click the ellipsis (three-dot) icon in the top-right corner to check additional action options.

![][image99]

5. Note that StoryMaps can be viewed in autoplay mode. To enable this feature, click the ellipsis (three-dot) icon and select **Turn autoplay on**.

![][image100]

6. You can also export your project as a PDF by selecting **Print preview** from the same menu.

![][image101]

7. Finally, you can save your project as a template by clicking **Save as template**. This allows you to reuse the same layout and assets in the future while simply replacing the content.

![][image102]

# **Resources**

ArcGIS Online offers a wide range of tools for visualizing and analyzing geospatial data, and in this tutorial we’ve only introduced a few. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

* [Transferring Data to a Public ArcGIS Account](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/Transferring%20Data%20to%20a%20Public%20ArcGIS%20Online%20Account.md), tutorial for long-term preservation for ArcGIS StoryMaps projects  
* [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;  
* [ArcGIS Story Maps Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online), blogs shared by the community;  
* [ArcGIS Story Maps Community Forum](https://community.esri.com/t5/arcgis-storymaps/ct-p/arcgis-storymaps) for asking questions and receiving answers or feedback.

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.