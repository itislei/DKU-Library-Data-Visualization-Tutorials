# **Storytelling with ArcGIS StoryMaps**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: March 3, 2026*

This tutorial introduces how to create map-based digital stories with ArcGIS StoryMaps.

# **Before we start**

## **Introduction**

In this tutorial, we will create a map-based digital story that explores airport data across China, building upon the spatial analysis conducted in ArcGIS Online. This demonstration StoryMap transforms spatial data into a clearer picture of national connectivity, presenting the analysis through a structured and engaging narrative format.

Because this tutorial uses the web map and layers developed in the [ArcGIS Online tutorial](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/ArcGIS%20Online/ArcGIS%20Online%20for%20Mapping%20Data%20and%20Spatial%20Analysis.md), it is recommended that you complete the ArcGIS Online tutorial before proceeding.

By the end of this tutorial, you will be able to use ArcGIS StoryMaps to design a digital narrative, [Mapping China’s Airports](https://arcg.is/uOT4q), that visualizes geographic distribution and communicates key analytical findings effectively.

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

<img width="1004" height="292" alt="image86" src="https://github.com/user-attachments/assets/25b350d6-09d7-426c-b05c-08d925a9293e" />


3. This will open the menu displaying all add-on products available under our institutional license. From the list, select **StoryMaps**.

<img width="469" height="340" alt="image1" src="https://github.com/user-attachments/assets/726dd2ef-cffc-4b70-bf4e-ffddbc2481c1" />


4. Now, you will be directed to ArcGIS StoryMaps.

# **Create a StoryMap**

1. Once you are in the ArcGIS StoryMaps, click on the **\+ Create** button on the upper right corner. Select **Story** from the dropdown list. You will be directed to a new page where you can begin adding and editing content.

<img width="353" height="286" alt="image36" src="https://github.com/user-attachments/assets/34ea56b5-bf62-4095-a72f-b3d316827472" />


2. In the new page, first, enter the story title by copying and pasting the content under \#1 in captions.docx into the title field.  
3. Copy and paste the content under \#2 into the StoryMap as the subtitle.

<img width="698" height="286" alt="image84" src="https://github.com/user-attachments/assets/ef8d99c7-9be0-4336-a030-d3034f5fb247" />

4. You may click on the **Change panel appearance** icon to adjust the alignment.

<img width="218" height="196" alt="image69" src="https://github.com/user-attachments/assets/1fa4a529-1aa1-4489-9491-dbb84c9abac6" />


5. Next, click the **Add cover image or video** button in the upper right corner. 

<img width="179" height="59" alt="image81" src="https://github.com/user-attachments/assets/385132d4-535d-4969-b31d-00e220ba59fa" />


6. In the pop-up window, click **Browse your files**.

<img width="478" height="477" alt="image18" src="https://github.com/user-attachments/assets/204e19f8-8ef1-4661-8412-13bab640a2cd" />

7. Navigate to the folder where the site images are stored, select **0\_Airplane\_on\_the\_Runway.jpg**, and click **Open**. 

<img width="935" height="540" alt="image95" src="https://github.com/user-attachments/assets/c0969591-c1d2-4de8-9ea4-f6d8dba97c75" />


8. Then click **Add**.

<img width="477" height="475" alt="image67" src="https://github.com/user-attachments/assets/2407c915-7871-4e0a-b610-7c5ce09119e4" />


9. You can adjust the image by clicking the **Options** (Settings) icon, or replace or delete it using the **More actions** (three-dot/ellipsis) icon.

<img width="260" height="139" alt="image35" src="https://github.com/user-attachments/assets/61703ff8-bf6d-4e3e-8aee-8e48884990e4" />


10. ArcGIS StoryMaps includes a variety of pre-made design themes that can be applied directly to your project. For example, click **Design** in the header to explore these options.

<img width="519" height="81" alt="image72" src="https://github.com/user-attachments/assets/ae99d033-c288-4f19-83fa-e0727c33c91e" />


11. The **Design** pane will open, allowing you to customize the appearance of your StoryMap using predefined themes and style elements. In this tutorial, we will use a specific design as an example, but you are welcome to choose the theme that best fits your preference.

<img width="520" height="151" alt="image" src="https://github.com/user-attachments/assets/f5bac998-012a-4b42-827d-cddec8695dfd" />


12. In this project, change the cover layout to **Side-by-side** and toggle on **Navigation**. We will configure the navigation menu later in the tutorial.

<img width="302" height="352" alt="image28" src="https://github.com/user-attachments/assets/70e9e8ea-3145-489d-91f7-8b785bece058" />


13. For the theme, select **Ridgeline**. You can explore additional options by clicking **Featured themes gallery**.

<img width="466" height="533" alt="image" src="https://github.com/user-attachments/assets/61f96b54-d52d-453a-a0a4-780eec1321ca" />


14. Once you have made your selections, close the **Design** pane.  
15. The cover has now been set up. Note that your changes are saved automatically.

<img width="975" height="490" alt="image" src="https://github.com/user-attachments/assets/c8f7a4d8-ccb8-4079-b820-6a98ee4d8275" />


# **Text Content**

1. Scroll below the cover to the blank area, click the **\+** button, and select **Text**.

<img width="426" height="412" alt="image" src="https://github.com/user-attachments/assets/6c775c2d-df41-4366-b32e-67c8aaa5cd93" />


2. Copy and paste the content under \#1 in captions.docx into the text box. Note that text separated by blank lines will automatically be divided into individual text blocks.

<img width="918" height="324" alt="image" src="https://github.com/user-attachments/assets/01d5c814-b306-4ee5-8366-9805249b3a1b" />


3. Triple click to highlight **“About the Project”**, then switch the font from **Paragraph** to **Heading 1**.

<img width="653" height="355" alt="image" src="https://github.com/user-attachments/assets/2cd93478-1c21-4130-874e-6ad472a61ba8" />


4. **“About the Project”** is now formatted as a larger, bold heading. It also appears in the navigation menu for easier access.

<img width="975" height="275" alt="image" src="https://github.com/user-attachments/assets/7f6ce384-d127-42f3-85b3-053b45d83082" />


5. Next, select the quote below “About the Project”, then switch the font from **Paragraph** to **Quote**.

<img width="975" height="508" alt="image" src="https://github.com/user-attachments/assets/c311b33b-98b6-4189-981a-112e00dae173" />


6. Copy and paste the content from section \#2 in captions.docx into the quote source box, then click outside the box to save your changes. Leave the last paragraph in this section as the default text.

<img width="975" height="438" alt="image" src="https://github.com/user-attachments/assets/d5925469-0dc1-402f-8b95-8648676833f4" />


# **Table**

1. Below the content added so far, click the **\+** icon to insert one **separator** and one text asset. Then copy and paste the content from section \#3 in captions.docx into the text box.

<img width="975" height="429" alt="image" src="https://github.com/user-attachments/assets/fe367c29-76dc-4771-be1e-6d5b0c33a13c" />


2. For **“Map 1”,** switch the font from **Paragraph** to **Heading 1**, and for **“Provinces with More Than 10 Airports”**, switch the font from **Paragraph** to **Heading 2**.

<img width="975" height="323" alt="image" src="https://github.com/user-attachments/assets/09c9229d-611f-4ef0-85d7-13a495838bde" />


3. Below the text, click the \+ icon and select Table from the list.

<img width="975" height="592" alt="image" src="https://github.com/user-attachments/assets/3063591d-2388-4c9e-a084-845d6ca1d65e" />


4. Copy and paste the table values from section \#4 in captions.docx into the table. Note that importing data from an existing file is not supported, and you cannot paste all content at once. You will need to copy and paste the content into each cell individually.  
5. If you need additional rows or columns, hover along the table edges and click the three-dot (ellipsis) icon. Then select **Insert row below** to add them.

<img width="862" height="355" alt="image" src="https://github.com/user-attachments/assets/544f2203-272e-4606-a218-d339c064c668" />


6. Lastly, after entering all the data into the table, add a caption below the table using the content from section \#5 in captions.docx.

<img width="975" height="771" alt="image" src="https://github.com/user-attachments/assets/eb8dc7f9-38fe-43d4-a729-208981d8191e" />


# **Charts**

1. Continue the Map 1 section, click on the **\+** icon and select **Chart** from the list.

<img width="892" height="789" alt="image" src="https://github.com/user-attachments/assets/136a62cb-6d5c-4956-b882-6db2f037d5b3" />


2. Select **Bar chart** from the options and click **Done**.

<img width="771" height="768" alt="image" src="https://github.com/user-attachments/assets/17f08258-35ff-4b1b-bc07-b687bd7255f8" />


3. In the left pane of the new page, copy and paste the content from section \#6 in captions.docx into the table. Note that importing data from an existing file is not supported, and you cannot paste all content at once. You will need to enter the content into each cell individually. Adding multiple columns of data is supported.

<img width="564" height="442" alt="image" src="https://github.com/user-attachments/assets/d07cc068-2af9-4ec6-891c-92ba75fa8d31" />


4. Switch to **Settings** from **Data** tab, copy and paste 

<img width="624" height="230" alt="image" src="https://github.com/user-attachments/assets/317f6edf-3fbd-49ac-9411-37e817a6bb96" />


5. Remove the values under **Chart title**, enter **Region of China** in the **Category axis title** field, and **Count of Provinces** in the **Value axis title** field.

<img width="594" height="403" alt="image" src="https://github.com/user-attachments/assets/78d56198-0e16-4297-9b18-4ef29a8bf2c8" />


6. Toggle on **Customize axis**, and enter **3** in the field.

<img width="588" height="217" alt="image" src="https://github.com/user-attachments/assets/c72c0ad2-549b-4d5b-b206-5d98ea85257a" />


7. Review the changes and click **Save** to confirm.

<img width="818" height="540" alt="image" src="https://github.com/user-attachments/assets/8076ec88-b145-444d-ad76-42eff4312a16" />


8. Back to the project, click **Add another block** as we are going to add the donut chart.

<img width="415" height="336" alt="image" src="https://github.com/user-attachments/assets/039c4c8f-39d0-4ede-abf6-85385c44c36b" />


9. Select **Donut chart** from the options and click **Done**.

<img width="691" height="683" alt="image" src="https://github.com/user-attachments/assets/fb378fae-3330-4469-9278-762af5b94ea0" />


10. Again, copy and paste the content under \#6 in captions.docx into the table on the left pane of the new page. Note that the donut chart can only work with two data columns.

<img width="623" height="550" alt="image" src="https://github.com/user-attachments/assets/09ccbd7c-6205-4600-9d69-0ae5f52ca3e2" />


11. Switch to the **Settings** tab and delete all content in the **Chart title** field.

<img width="500" height="677" alt="image" src="https://github.com/user-attachments/assets/55af9ee6-8161-4494-a9e2-74536ac310ed" />


12. Review the chart, then click **Save** when it's ready.

<img width="846" height="557" alt="image" src="https://github.com/user-attachments/assets/2cc5e81b-548c-4bf1-ba6a-cd914a5f4319" />


13. Return to the project, then copy the content from section \#7 in captions.docx and paste it under the charts as the caption. Click anywhere outside the box to save the changes. 

<img width="975" height="390" alt="image" src="https://github.com/user-attachments/assets/a073b5f4-db92-469a-a5b5-80b544e206ca" />


14. You may add another chart by clicking the **Add another block** icon, but note that a maximum of three charts is allowed per row.

<img width="975" height="383" alt="image" src="https://github.com/user-attachments/assets/4801bd52-27a8-4ef8-bace-28d94b7d491e" />


# **Web Map**

1. Below the charts, click on the **\+** icon and select **Map** from the list.

<img width="975" height="633" alt="image" src="https://github.com/user-attachments/assets/77fdc6b3-488c-4a82-99f5-c9675a028194" />


2. On the new page, if you followed and completed the ArcGIS Online tutorial, you should be able to find your web map project saved under **My Content**. Click on it to continue.

<img width="975" height="602" alt="image" src="https://github.com/user-attachments/assets/23f859e3-01ba-49be-8ebd-f591d87da638" />


3. If you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly.

<img width="975" height="602" alt="image" src="https://github.com/user-attachments/assets/8d0ebbad-0f45-4694-a343-c2264e2a4483" />


4. Under **Layers** tab, make sure that **Count of airports in provinces** and **China Province Boundaries** layers are visible as all others are hidden.  
5. Under **Layers** tab, make sure that **Chinese provinces with other 10 airports** and **China Province Boundaries** layers are visible as all others are hidden.

<img width="450" height="454" alt="image" src="https://github.com/user-attachments/assets/3179a66d-bfd1-47b8-bad9-c64f3590bc59" />


6. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level, then click **Save** to continue.

<img width="975" height="685" alt="image" src="https://github.com/user-attachments/assets/30ea9545-a821-4193-a128-1e3fd951491f" />


7. Back to the project, copy the content from section \#8 in captions.docx and paste it under the map as the caption.

<img width="975" height="583" alt="image" src="https://github.com/user-attachments/assets/df584f87-52e8-4aef-8858-ad15bdbc75a3" />


8. Hover over the map, and a toolbar will appear. From there, you can edit the map view, adjust the view window, or remove the map.

<img width="768" height="252" alt="image" src="https://github.com/user-attachments/assets/a8aa5ac5-9c6d-496c-a945-63950c85d732" />


9. In the next line, click **\+** icon to add a new separator.

<img width="960" height="598" alt="image" src="https://github.com/user-attachments/assets/ea80b0f4-f90a-45ea-a191-38ccd53a53e7" />


# **Sidecar**

1. Below the web map, click on the **\+** icon and select **Text** from the list.  
2. Copy and paste the content under \#9 in captions.docx into the text box. Change the font style of **“Map 2”** from Paragraph to **Heading 1**, and **“Airport Counts Across All Provinces”** to **Heading 2**.

<img width="830" height="283" alt="image" src="https://github.com/user-attachments/assets/1c2b3842-e17a-4b0d-8e9f-75df28424717" />


3. Below the text box, click on the **\+** icon and select **Sidecar** from the list.

<img width="582" height="580" alt="image" src="https://github.com/user-attachments/assets/7e3fcaee-d4b7-42e7-8531-89fe61944c12" />


4. From the options, select **Floating** and click **Save**.

<img width="583" height="712" alt="image" src="https://github.com/user-attachments/assets/ba336196-2886-4a14-8dae-540e97dc670e" />


5. Under the navigation, click on **\+ Add** button.

<img width="672" height="275" alt="image" src="https://github.com/user-attachments/assets/5a556a6b-a20b-4a52-a0fc-99ea83688495" />


6. Select **Map** from the options.

<img width="304" height="615" alt="image" src="https://github.com/user-attachments/assets/23d300c9-84fb-4ff7-9de5-f1b684523efb" />


7. On the new page, if you followed and completed the ArcGIS Online tutorial, you should be able to find your web map project saved under **My Content**. Click on it to continue. If you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly.

<img width="975" height="602" alt="image" src="https://github.com/user-attachments/assets/6d8fc825-589b-446e-bfb3-bc77ab6f0502" />


8. Under **Layers** tab, make sure that **Count of airports in provinces** and **China Province Boundaries** layers are visible as all others are hidden.

<img width="532" height="446" alt="image" src="https://github.com/user-attachments/assets/6a0dec47-77ee-475d-acbe-88ed7293328e" />


9. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level, then click **Save** to continue.

<img width="975" height="565" alt="image" src="https://github.com/user-attachments/assets/156b168b-a4fc-441c-bb63-cab25e6d72ef" />


10. You may use the floating toolbar to adjust the map view.

<img width="372" height="153" alt="image" src="https://github.com/user-attachments/assets/a36bebba-f25d-4a54-b831-d3e8b79de561" />


11. Copy and paste content under \#10 in captions.docx to the left text box.

<img width="863" height="499" alt="image" src="https://github.com/user-attachments/assets/4b1ab742-5b84-485d-92a1-ecad05351bf3" />


12. You may adjust the look of the text. For example, make“higher counts” and “larger and darker” a bold and darker color, while making “fewer airports” and “smaller and lighter” a brighter color.

<img width="619" height="286" alt="image" src="https://github.com/user-attachments/assets/1d6e7f4c-5f31-4035-833d-6fa5835abb0a" />


13. Click on the **\+** icon at the bottom right. We are going to add another slide here.

<img width="975" height="156" alt="image" src="https://github.com/user-attachments/assets/1fa24475-9ec0-49ae-ac96-6edb2deb5ea4" />


14. Click on **\+ Add** button and select **Map** from the options. On the new page, open the ArcGIS Online tutorial project either created by yourself under **My Content**, or the one under **My Organization** created by the instructor (if you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly).   
15. Note that there are two dots that are the smallest and brightest on the map. First, zoom in on the top one.

<img width="673" height="445" alt="image" src="https://github.com/user-attachments/assets/1b75a0ce-fb95-43bc-94b2-9fdaa30d0991" />


16. Make sure the dot is in the center, then click **Save** to continue.    

<img width="975" height="565" alt="image" src="https://github.com/user-attachments/assets/657a224b-31f2-436a-935e-a20d7e343d36" />


17. Copy and paste content under \# 11in captions.docx to the left text box.

<img width="975" height="419" alt="image" src="https://github.com/user-attachments/assets/4fd956ee-086c-477e-86c8-e6231673911b" />


18. Repeat the same step and add another slide with the other white dot at the bottom map, along with the corresponding content under \#12 in captions.docx.

<img width="975" height="379" alt="image" src="https://github.com/user-attachments/assets/3dc7843f-fb9f-4df6-b175-71b0c4229ff9" />


19. Scroll down to the sidecar section below and add a **separator** to continue.

# **Swipe**

1. Below the web map, click the **\+** icon and select **Text** from the list. Copy and paste the content under \#13 in captions.docx into the text box. Then change the font style of **“Map 3”** from **Paragraph** to **Heading 1**, and change **“Airport Locations in Jiangsu Province”** to **Heading 2**.  
2. Below the text, click the **\+** icon and select **Swipe**.

<img width="762" height="507" alt="image" src="https://github.com/user-attachments/assets/b99e628b-05e7-48fc-9193-1eda6a8fabef" />


3. First, click on **Add media** on the left pane.

<img width="975" height="588" alt="image" src="https://github.com/user-attachments/assets/15c99bb1-50be-482f-a482-0f1f9ccbabd6" />


4. Select **Web Map** from the options. Note that you can also add an image (e.g., scan of physical map) here.

<img width="417" height="347" alt="image" src="https://github.com/user-attachments/assets/f6617ef5-b08a-4dda-a8ae-75e36e97464a" />


5. On the new page, again, select the ArcGIS Online tutorial project either created by yourself under **My Content**, or the one under **My Organization** created by the instructor (if you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly).   
6. Under **Layers** tab, make sure that **Airports in Jiangsu** and **China Province Boundaries** layers are visible as all others are hidden.

<img width="619" height="625" alt="image" src="https://github.com/user-attachments/assets/b929836a-dcf4-4d58-8754-3e0c9afd394c" />


7. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level. Make sure Jiangsu Province is centered and clearly visible on the view, then click **Save** to continue.

<img width="975" height="565" alt="image" src="https://github.com/user-attachments/assets/71004b40-3c01-48f2-8b0f-a3038067be62" />


8. Click on **Add web map** at the right pane.

<img width="975" height="583" alt="image" src="https://github.com/user-attachments/assets/211bcd26-7f67-417d-9bf4-89998f28c628" />


9. Now, filter to **Living Atlas** and **World**, then pick an option from the result list. For this tutorial, let’s pick up **Open Basemap (Streets)**.

<img width="975" height="652" alt="image" src="https://github.com/user-attachments/assets/b5e82186-ad21-4c22-892b-5a7bbe297da3" />


10. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level. Make sure Jiangsu Province is centered and clearly visible on the view, then click **Save** to continue.

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/63a1187b-eea8-403a-8eff-157e528c9bb7" />


11. If you think the visibility level needs changes, you can always click on the **Edit** icon under each map in the swipe to change it.

<img width="975" height="573" alt="image" src="https://github.com/user-attachments/assets/6a1a4fae-2e39-40f1-bb68-5f042cab8ea4" />


12. Once you have finished editing the map, drag the **Swipe** icon across the map to compare the layers. You can also use the **Zoom In** and **Zoom Out** icons to adjust the visibility level.

<img width="975" height="556" alt="image" src="https://github.com/user-attachments/assets/82d17d15-2a20-41f7-b452-be33fc3bc4fe" />


13. Don’t forget to add a caption to the maps. Copy and paste the content under \#14 in the caption file.

<img width="975" height="583" alt="image" src="https://github.com/user-attachments/assets/6ca2683c-54e7-4f71-ba92-093a20294e65" />


14. Lastly, hover over the edges of the map and click **Medium** in the floating toolbar. This will enlarge the map view.

<img width="570" height="188" alt="image" src="https://github.com/user-attachments/assets/ad19ac3f-fced-4d2b-9a9f-474fca59e77a" />


15. In the new section below, add a **separator** to continue.

# **Map Tour**

1. Below the swipe, click the **\+** icon and select **Text** from the list. Copy and paste the content under \#15 in captions.docx into the text box. Then change the font style of **“Map 4”** from **Paragraph** to **Heading 1**, and change **“Three Closest Airports to DKU”** to **Heading 2**.  
2. Below the text, click the \+ icon and select **Map tour**.

<img width="798" height="841" alt="image" src="https://github.com/user-attachments/assets/598658a9-3d58-4ce0-8907-e48411ce7e6c" />


3. From the options, select **Upload photos**.

<img width="975" height="463" alt="image" src="https://github.com/user-attachments/assets/a2b4dc19-a070-4327-a089-087ce039a3f3" />


4. Click **Browse your files**.

<img width="649" height="651" alt="image" src="https://github.com/user-attachments/assets/c9540473-8af3-4697-99ca-f157a1d162df" />


5. Navigate to the sites folder from the sample datasets, and select all image files except 0\_Airport\_on\_Runway, then click **Open**. To select multiple files at once, click the first item, press the **Shift** key on your keyboard, and then click the last item to select all at once.

<img width="975" height="565" alt="image" src="https://github.com/user-attachments/assets/76e236c7-0d61-4a7d-a785-27b2e9ec3aad" />


6. Make sure 4 images are selected, click **Add**.

<img width="562" height="559" alt="image" src="https://github.com/user-attachments/assets/eadec93e-29a7-415b-af91-32a37bdb88e4" />


7. For the layout, select **List** under **Explorer tour**, and click **Save**.

<img width="679" height="766" alt="image" src="https://github.com/user-attachments/assets/cb773d07-5c8e-4fb5-8743-86f034137c20" />


8. Copy and paste the content under \#16 in captions.docx as the title and \#17 as the description for the first image into the text box.

<img width="975" height="473" alt="image" src="https://github.com/user-attachments/assets/589da812-1f59-4672-83f9-1e9cfd5950f3" />


9. Next, open **Map\_tour\_data.csv** on your local computer. Drag and select the values under **LAT** and **LNG** for **Duke Kunshan University**.

<img width="975" height="340" alt="image" src="https://github.com/user-attachments/assets/8ac44b40-3481-471c-8d99-830126059de5" />


10. Right-click and select **Copy**. Alternatively, press **Ctrl \+ C** on Windows (or **Command \+ C** on Mac) to copy.

<img width="610" height="341" alt="image" src="https://github.com/user-attachments/assets/26230c45-a683-4823-b3c6-1e7b06bdee10" />


11. Go back to the StoryMap and click **Add location** on the **Duke Kunshan University** card.

<img width="543" height="337" alt="image" src="https://github.com/user-attachments/assets/e6624063-cbe6-4bc2-8b87-d77849c1683a" />


12. On the new page, paste the values into the search box in the top-right corner. A dropdown list of matching place names will appear. However, since we are searching by coordinates, press **Enter** to commit the search.

<img width="975" height="525" alt="image" src="https://github.com/user-attachments/assets/e4af551d-808b-4a64-9ee7-d8f4f5b2e527" />


13. This will take you to a location near the DKU campus. Zoom out slightly and you will notice the marker is a bit off. Click **Close**, then reselect the correct location. If you are satisfied with the updated location, click **Add to map** to confirm.

<img width="975" height="508" alt="image" src="https://github.com/user-attachments/assets/57474107-f306-4fdd-9842-9385dc7a23b5" />


14. Move your cursor to the center of DKU and click to place a marker.

<img width="691" height="443" alt="image" src="https://github.com/user-attachments/assets/d81343c2-94c5-4290-a320-833c58a23049" />


15. Set the visibility level to **Use the current zoom level**, then click **Save**.

<img width="443" height="389" alt="image" src="https://github.com/user-attachments/assets/e1e9b0da-fbcd-4b00-81b0-eb3c0b7f5b76" />


16. Once editing is complete, switch to the second image from the bottom of the list, or use the mouse wheel to continue making changes.  
17. Repeat steps (\#8–15) to complete the information for the remaining three images.  
18. Then scroll down to the map tour section below and add a **separator** to continue.

# **Credits**

1. In the blank area, create a new text box and copy and paste the content under \#24 in captions.docx into the text box. Change the font style to **Heading 1**.  
2. Then create another text box below. Copy and paste the image source titles under \#25 in captions.docx into this text box.  
3. Select each line of text, click **Link**, and hyperlink the titles using the corresponding URLs listed under \#26 in captions.docx.

<img width="816" height="293" alt="image" src="https://github.com/user-attachments/assets/6365afdd-cf41-43f5-948c-c1f8767da81a" />


4. Scroll down to the bottom of the page, and add your self author credits. 

<img width="975" height="292" alt="image" src="https://github.com/user-attachments/assets/4ac4e7db-c4fa-48ff-a940-2b623c6740d0" />


# **Publish the StoryMap**

1. Once completed the editing, Go to the top menu and click **Publish**.

<img width="681" height="139" alt="image" src="https://github.com/user-attachments/assets/a52df20d-b2f6-4f3d-9caf-7dcf6940ce05" />


2. You may change the title, subtitle, cover by clicking on the **Edit** on the left pane.

<img width="613" height="712" alt="image" src="https://github.com/user-attachments/assets/c5fc0fc0-1780-4688-a876-54f425a48d53" />


3. On the right pane, set the sharing level to **Organization**.

<img width="518" height="549" alt="image" src="https://github.com/user-attachments/assets/7fcb1d1a-05cb-4703-91f8-beeed2507210" />


4. If you have a group or collaborating with others, you may set the **group sharing**.

<img width="582" height="616" alt="image" src="https://github.com/user-attachments/assets/1ed427a3-55e0-4ac9-a1f4-844deee2dc68" />


5. You may also set some advanced options for the sharing, such as allowing others to duplicate or showing your project in the web search results if you set the project to be visible to the public.  
6. When everything is set, click **Publish**.

<img width="582" height="616" alt="image" src="https://github.com/user-attachments/assets/150c8a20-aa7f-478e-ab6e-837104c24f2c" />


7. Now the project should be published. And there are several ways to share it to others and view.

<img width="550" height="194" alt="image" src="https://github.com/user-attachments/assets/e66bd143-7f25-42af-bab1-7de5315e9a58" />


# **View and Save StoryMap**

1. After the project is completed, you may click on the View published story button, or copy the link and open in a new tab, or scan the QR code to open. You may also share the link or the QR code.

<img width="511" height="656" alt="image" src="https://github.com/user-attachments/assets/9a127dbe-0729-4297-8d5d-1b239cb84fac" />


2. You can always find the projects or drafts in your [StoryMaps content](https://storymaps.arcgis.com/content).   
3. In the project, you may use the mouse wheel and cursor to scroll through and review the content.  
4. Click the ellipsis (three-dot) icon in the top-right corner to check additional action options.

<img width="569" height="166" alt="image" src="https://github.com/user-attachments/assets/8bc92819-e4d4-4ada-a7bd-03db1885f1e6" />


5. Note that StoryMaps can be viewed in autoplay mode. To enable this feature, click the ellipsis (three-dot) icon and select **Turn autoplay on**.

<img width="466" height="493" alt="image" src="https://github.com/user-attachments/assets/506e67c1-4669-4d53-aa39-ddf332bbad19" />


6. You can also export your project as a PDF by selecting **Print preview** from the same menu.

<img width="468" height="543" alt="image" src="https://github.com/user-attachments/assets/d588cd77-cf15-4702-8888-67c789560464" />


7. Finally, you can save your project as a template by clicking **Save as template**. This allows you to reuse the same layout and assets in the future while simply replacing the content.

<img width="457" height="530" alt="image" src="https://github.com/user-attachments/assets/32178392-679a-40ee-8214-c46285c01f73" />


# **Resources**

ArcGIS Online offers a wide range of tools for visualizing and analyzing geospatial data, and in this tutorial we’ve only introduced a few. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

* [Transferring Data to a Public ArcGIS Account](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/Transferring%20Data%20to%20a%20Public%20ArcGIS%20Online%20Account.md), tutorial for long-term preservation for ArcGIS StoryMaps projects  
* [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;  
* [ArcGIS Story Maps Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online), blogs shared by the community;  
* [ArcGIS Story Maps Community Forum](https://community.esri.com/t5/arcgis-storymaps/ct-p/arcgis-storymaps) for asking questions and receiving answers or feedback.

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.
