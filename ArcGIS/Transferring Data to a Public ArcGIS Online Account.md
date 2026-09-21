# **Transferring ArcGIS Online Content from an Institutional Account to a Public Account**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: September 20, 2026*

This tutorial explains how to preserve items and projects stored in ArcGIS Online, and use [ArcGIS Assistant](https://assistant.esri-ps.com/) to transfer from an institutional account to a public or another institution’s account. It also provides a quick overview of how other common item types are handled. For detailed help with more item types, see the resources at the end.

### **Contents**

- [Before You Start](#before-you-start)
  - [About ArcGIS Assistant](#about-arcgis-assistant)
  - [Limitations](#limitations)
- [Understand How Items Are Connected](#understand-how-items-are-connected)
  - [What Happens to Each Item Type During Transfer](#what-happens-to-each-item-type-during-transfer)
- [Create ArcGIS Public Account](#create-arcgis-public-account)
- [Download Items Directly from ArcGIS Online](#download-items-directly-from-arcgis-online)
  - [Map Layer](#map-layer)
  - [Dataset](#dataset)
- [Convert and Upload a Dataset](#convert-and-upload-a-dataset)
  - [Convert the XLSX File to CSV](#convert-the-xlsx-file-to-csv)
  - [Add the CSV as a Map Layer](#add-the-csv-as-a-map-layer)
  - [Upload the CSV as a File Item](#upload-the-csv-as-a-file-item)
- [Transfer Items Using ArcGIS Assistant](#transfer-items-using-arcgis-assistant)
  - [Sign In to ArcGIS Assistant](#sign-in-to-arcgis-assistant)
  - [Copy Items to Your Personal Account](#copy-items-to-your-personal-account)
  - [Transfer Items That Cannot Be Copied Directly](#transfer-items-that-cannot-be-copied-directly)
- [After Transfer](#after-transfer)
  - [CSV Shapefile GeoJSON and CSV Collection](#csv-shapefile-geojson-and-csv-collection)
  - [Web Map](#web-map)
  - [StoryMap](#storymap)
  - [Hosted Feature Layer](#hosted-feature-layer)
  - [Final Check](#final-check)
- [Resources](#resources)

### **Before You Start**

#### **About ArcGIS Assistant**

[ArcGIS Assistant](https://assistant.esri-ps.com/) is a web-based tool for viewing and copying ArcGIS Online items between accounts. This tutorial uses the tool to copy supported content from an institutional account to a public or another institutional account.

#### **Limitations**

In ArcGIS Online, a public account is free and different from an institutional account. Some features and tools available through the institutional license may not be available with a public account. You can **only migrate items that you own**. For items you do not have permission to migrate, please contact the item owner.

### **Understand How Items Are Connected**

An ArcGIS project is often a group of connected items, not a single file. The diagram below shows the workflow of creating a storymap.

```mermaid
flowchart LR
    A["Datasets<br/>Source files<br/>CSV · Excel · Shapefile · GeoJSON<br/>CSV Collection"]
    B["Hosted Feature Layer<br/>Stores geographic data online"]
    C["Web Map<br/>Uses one or more layers"]
    D["StoryMap<br/>Combines a Web Map with text and media"]
    A -->|Can be published as| B
    B -->|Can be used in| C
    C -->|Can be added to| D
    classDef item fill:#f5f7fb,stroke:#2f6688,color:#111,stroke-width:1.5px;
    class A,B,C,D item;
```

A StoryMap can be copied directly, but its web maps and hosted layers are not automatically copied with it. If those connected items also need to move, handle them from top to bottom: source data and hosted layers first, then the web map, and finally the StoryMap.

#### **What Happens to Each Item Type During Transfer**

Use this table to see how common ArcGIS Online item types move and whether they still depend on the institutional account after migration.

| **Item type** | **How to transfer it** | **After the transfer** |
| --- | --- | --- |
| **CSV, Shapefile, and CSV Collection** | Use ArcGIS Assistant. | You own the copied file or collection. It no longer depends on the institutional account. |
| **Microsoft Excel** | Download the .xlsx file. | The file is saved on your computer. Upload a CSV copy if you want to use the table in your Public Account. |
| **Feature Service or Hosted Feature Layer** | Can not transfer entirely. Select Copy by reference. | Your account receives a link to the layer in the institutional account. The data stays in the institutional account. |
| **Feature Layer** | If exporting is available, export the layer as a GeoJSON file and upload it to the new account. Otherwise, select Copy by reference. | A GeoJSON upload creates an independent copy of the features and attributes. Copy by reference continues to use the original layer in the institutional account. |
| **Web Map** | Use ArcGIS Assistant. | You own the copied Web Map. Its layers still use their original item IDs or URLs until you move and reconnect them. |
| **StoryMap, Collection, or Theme** | Use ArcGIS Assistant. | You own the copied item. Text and uploaded media move with it, but embedded maps, layers, and web links stay connected to their original sources. |
| **Dashboard, Instant App, or Experience Builder app** | Use ArcGIS Assistant. | You own the copied app item. Its maps, layers, and services may still come from the institutional account. |
| **Survey123 or Field Maps content** | Move the form or app together with its maps and layers. | These items work as a set. Moving only the form or app leaves it connected to content in the institutional account. |
| **Map, image, vector tile, WMS, WFS, or other service layer** | Can not transfer entirely. Select Copy by reference. | Your account receives a link. The service stays at its original URL and does not move into your account. |
| **KML or KMZ, GeoPackage, file geodatabase, images, documents, or ArcGIS Pro packages** | Download the file. Upload it if your Public Account accepts the format. | The downloaded or uploaded file is yours and no longer depends on the institutional account. |

If you have questions about transferring other item types, contact the Data and Visualization Librarian ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for help.

### **Create ArcGIS Public Account**

Before you begin, make sure you have access to two accounts: your **source account**, where your existing items are stored, and your **destination account**, where you want to transfer the items. If you need a destination account, follow the steps below to create a free ArcGIS public account.

1. Go to [ArcGIS Online](https://www.arcgis.com/) and click **Sign In**.

<p align="center"><img width="517" alt="Go to ArcGIS Online and click Sign In" src="https://github.com/user-attachments/assets/29bc5928-1246-4618-9505-5e1bd1e590f4" /></p>

2. At the bottom of the sign-in window, click **Create an account**.

<p align="center"><img width="317" alt="At the bottom of the sign-in window, click Create an account" src="https://github.com/user-attachments/assets/32bb5f8d-c9c8-466c-a6d1-109d51793174" /></p>

3. Under **Create a public account**, click **Create an account**.

<p align="center"><img width="517" alt="Under Create a public account, click Create an account" src="https://github.com/user-attachments/assets/f4c71c38-da39-4d70-8a8d-010a22de2e01" /></p>

4. Enter your **first name**, **last name**, and **email address**. Accept the Esri Master License Agreement and Privacy Statement, then click **Next**.

<p align="center"><img width="317" alt="Enter your first name, last name, and email address. Accept the Esri Master License Agreement and Privacy Statement, then click Next." src="https://github.com/user-attachments/assets/aa7ade5c-e00a-4d42-bb6f-e094d684b62c" /></p>

5. ArcGIS will send an activation email to the email address you entered. Open your **email inbox** to continue.

<p align="center"><img width="317" alt="ArcGIS will send an activation email to the email address you entered. Open your email inbox to continue." src="https://github.com/user-attachments/assets/f15b8121-a972-4615-91fc-3ca9d41ef9af" /></p>

6. Open the email from the ArcGIS Accounts Team and click the **activation link**. The link expires after 24 hours.

<p align="center"><img width="517" alt="Open the email from the ArcGIS Accounts Team and click the activation link. The link expires after 24 hours." src="https://github.com/user-attachments/assets/cc2c80d0-f48b-487f-995e-d68e74eedaed" /></p>

7. Create a **username** and **password**, select a **security question**, and enter your answer. Then click **Create account**.

<p align="center"><img width="317" alt="Create a username and password, select a security question, and enter your answer. Then click Create account." src="https://github.com/user-attachments/assets/c0f7d891-8fd2-4b93-b037-0156b09acb5b" /></p>

8. After the account is created, open the account menu in the upper-right corner and confirm that you are signed in to your new ArcGIS public account.

<p align="center"><img width="317" alt="After the account is created, open the account menu in the upper-right corner and confirm that you are signed in to your new ArcGIS public account." src="https://github.com/user-attachments/assets/d930cced-a209-4db8-91af-a808e40c96ff" /></p>

### **Download Items Directly from ArcGIS Online**

Use this method when you want to keep the data from a hosted feature layer. Export the layer as a GeoJSON file from your institutional account, then upload it to your public account. This method does not require ArcGIS Assistant. The features and attributes transfer with the file, but you may need to recreate symbols and other layer settings.

For this part, we use the Feature layer (hosted) and Microsoft Excel spreadsheet as our example.

#### **Map Layer**

For this section, we use a **Feature layer (hosted)** as an example.

1. Follow the [ArcGIS Online sign-in tutorial](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/Signing%20In%20to%20ArcGIS.md) to sign in with your institutional account.

2. Open **Content**, then select a **Feature layer (hosted)** item that you own.

<p align="center"><img width="317" alt="Open Content, then select a Feature layer (hosted) item that you own." src="https://github.com/user-attachments/assets/0485d5be-1a11-46a7-8938-83db0ff8def4" /></p>

3. On the item page, open **Overview**, select **Export Data**, and choose **Export to GeoJSON**.

<p align="center"><img width="317" alt="On the item page, open Overview, select Export Data, and choose Export to GeoJSON." src="https://github.com/user-attachments/assets/a6f3802d-3908-42bf-9d0c-e4b669f47e19" /></p>

4. Enter a **Title**, choose a folder, and click **Export**.

<p align="center"><img width="317" alt="Enter a Title, choose a folder, and click Export." src="https://github.com/user-attachments/assets/713fb0c1-4889-48c7-ba50-4345d26030b7" /></p>

5. On the new item page, open **Overview** and click **Download**. Make sure the file is saved on your computer.

<p align="center"><img width="317" alt="On the new item page, open Overview and click Download. Make sure the file is saved on your computer." src="https://github.com/user-attachments/assets/55fcdaee-7b89-438e-a344-42f70e24fbc2" /></p>

6. Next, sign in to your personal public account in ArcGIS Online.

7. Select **Map** tab to open Map Viewer.

<p align="center"><img width="517" alt="Select the Map tab to open Map Viewer." src="https://github.com/user-attachments/assets/10874154-174b-4969-a825-098ad78a7c27" /></p>

8. On the left toolbar, select **Add**, then choose **Add layer from file**.

<p align="center"><img width="517" alt="On the left toolbar, select Add, then choose Add layer from file." src="https://github.com/user-attachments/assets/4c74af82-4145-49e3-8f31-fa671e4300e5" /></p>

9. Find the location where GeoJSON file was saved, then select the downloaded **.geojson** file and click **Open**.

<p align="center"><img width="517" alt="Find the location where the GeoJSON file was saved, select the downloaded .geojson file, and click Open." src="https://github.com/user-attachments/assets/09a3790d-b924-439e-8ccf-004c51899318" /></p>

10. In the pop-up, click **Create and add to map**, and wait for the process to complete. Larger files may take longer to process.

11. On the left toolbar, select **Save and open**, then select **Save as**.

<p align="center"><img width="517" alt="On the left toolbar, select Save and open, then select Save as." src="https://github.com/user-attachments/assets/6380bdcb-08e9-4520-99e7-195d7defc2f8" /></p>

12. Enter a **Title** and click **Save**.

<p align="center"><img width="317" alt="Enter a Title and click Save." src="https://github.com/user-attachments/assets/0fffb354-78c1-4674-a361-86811d36f30f" /></p>

13. Go to **Content**. The file should be now saved in your public account.

#### **Dataset**

For this section, we use a **Microsoft Excel spreadsheet** as an example.

1. In ArcGIS Online, log in to your institutional account. Then, go to **Content**, locate an **Excel item**, and then click **Preview**.

<p align="center"><img width="517" alt="In ArcGIS Online, log in to your institutional account. Then, go to Content, locate an Excel item, and click Preview." src="https://github.com/user-attachments/assets/6293cdf5-d02c-4d5a-ba9a-6f75e86c1e23" /></p>

2. Go to the **details**, then click **Download**. The .xlsx file will be saved on your computer.

<p align="center"><img width="317" alt="Go to the details, then click Download. The .xlsx file will be saved on your computer." src="https://github.com/user-attachments/assets/b290152e-13f9-4ff9-9a5f-a4f3ff5c8afa" /></p>

### **Convert and Upload a Dataset**

Use Microsoft Excel to convert the downloaded **.xlsx** workbook to a **CSV UTF-8** file. Then add the CSV to a map in your ArcGIS public account.

#### **Convert the XLSX File to CSV**

1. Open Microsoft Excel on your computer, and select the downloaded **.xlsx** workbook under Recent.

<p align="center"><img width="517" alt="Open Microsoft Excel on your computer, and select the downloaded .xlsx workbook under Recent." src="https://github.com/user-attachments/assets/869c33cd-51cd-420d-a008-4f9fc549f8ab" /></p>

2. After the workbook opens, click **File**.

<p align="center"><img width="517" alt="After the workbook opens, click File." src="https://github.com/user-attachments/assets/81b47e9c-d666-45f9-8112-0e2cc2e65ffc" /></p>

3. Select **Save As**.

<p align="center"><img width="317" alt="Select Save As." src="https://github.com/user-attachments/assets/62cb2061-2fe1-4dcb-a578-cc5e841d7dca" /></p>

4. Choose a save location, enter a clear file name, and open the file-format menu.

<p align="center"><img width="517" alt="Choose a save location, enter a clear file name, and open the file-format menu." src="https://github.com/user-attachments/assets/8ef6790f-27d6-4d4f-b34d-abe972d6161d" /></p>

5. Select **CSV UTF-8 (Comma delimited) (.csv)**. UTF-8 helps preserve Chinese and other non-English characters.

<p align="center"><img width="517" alt="Select CSV UTF-8 (Comma delimited) (.csv). UTF-8 helps preserve Chinese and other non-English characters." src="https://github.com/user-attachments/assets/bc688c60-2ef1-49a6-8748-8e99231d2e0e" /></p>

6. Click **Save**.

<p align="center"><img width="517" alt="Click Save." src="https://github.com/user-attachments/assets/164a9172-48f5-4d85-b565-691066cfeb4c" /></p>

7. If Excel explains that CSV does not support multiple sheets, click **OK** to save the active sheet.

<p align="center"><img width="517" alt="If Excel explains that CSV does not support multiple sheets, click OK to save the active sheet." src="https://github.com/user-attachments/assets/2dfc505d-c35c-4485-8bdf-ce7c42e30ad3" /></p>

CSV files save only the active worksheet and the values shown in its cells. If the workbook contains **multiple worksheets**, save each worksheet as **a separate CSV file**. Formatting, charts, and other Excel features are not included. Keep the original **.xlsx** file as a backup.

#### **Add the CSV as a Map Layer**

Use this method when the CSV contains location information and you want to display the data on a map.

1. Sign in to ArcGIS Online with your public account and open **Map** to start Map Viewer.

2. Open **Layers**, click the arrow next to **Add**, and select **Add layer from file**.

<p align="center"><img width="517" alt="Open Layers, click the arrow next to Add, and select Add layer from file." src="https://github.com/user-attachments/assets/382a8914-2d8a-40dc-af50-4616b3050f70" /></p>

3. Select the CSV file saved from Excel. If ArcGIS asks how to locate the data, check that the correct latitude and longitude or address fields are selected.

4. Enter a **Title**, choose a folder, and click **Create and add to map**.

<p align="center"><img width="517" alt="Enter a Title, choose a folder, and click Create and add to map." src="https://github.com/user-attachments/assets/265fe83a-4584-4893-873c-4bc9773a059f" /></p>

5. Confirm that the new CSV layer appears in the **Layers** panel and displays correctly on the map.

#### **Upload the CSV as a File Item**

This optional method is useful if you only want to store the CSV in your account so it can be downloaded later. It does not add the data to a map.

1. In your public account, open **Content**, select **My content**, and click **New item**.

<p align="center"><img width="517" alt="In your public account, open Content, select My content, and click New item." src="https://github.com/user-attachments/assets/df3951d8-7ee5-4c40-860c-d77521c34cec" /></p>

2. Select **Your device** and choose the CSV file.

<p align="center"><img width="517" alt="Select Your device and choose the CSV file." src="https://github.com/user-attachments/assets/2a613929-4e9f-41df-950b-787387786ed6" /></p>

3. Enter a **Title**, choose a folder, add tags or a summary if needed, and click **Save**.

<p align="center"><img width="517" alt="Enter a Title, choose a folder, add tags or a summary if needed, and click Save." src="https://github.com/user-attachments/assets/5a001abb-9e38-4825-81da-aed36924fc85" /></p>

Other spreadsheet applications and file-conversion tools can also create CSV files. Before using an online converter, consider whether the data contains **private, sensitive, or restricted information** and review the tool's **privacy and security practices**.

For more information, see Esri's [Add layers from files](https://doc.arcgis.com/en/arcgis-online/create-maps/add-layers-from-file.htm) documentation.

### **Transfer Items Using ArcGIS Assistant**

In this section, we will use **ArcGIS Assistant** to transfer items between ArcGIS Online accounts. ArcGIS Assistant is a tool designed to help migrate content between accounts.

#### **Sign In to ArcGIS Assistant**

1. Open **ArcGIS Assistant** at [https://assistant.esri-ps.com/](https://assistant.esri-ps.com/) and click **Sign in** at the top right corner.

<p align="center"><img width="517" alt="Open ArcGIS Assistant at https://assistant.esri-ps.com/ and click Sign in at the top right." src="https://github.com/user-attachments/assets/7df9208f-564c-474b-aa3d-3a6bccacc57f" /></p>

2. Type **“Dukeuniv”** to sign in to your institutional ArcGIS Online account.

<p align="center"><img width="317" alt="Type “Dukeuniv” to sign in to your institutional ArcGIS Online account." src="https://github.com/user-attachments/assets/d753ae4e-9349-4a64-80ad-27371642d12f" /></p>

<p align="center"><img width="317" alt="Select Duke University to continue signing in to your institutional ArcGIS Online account." src="https://github.com/user-attachments/assets/e137e034-2b06-440c-87b8-0b11ff5f13cb" /></p>

3. Select **My Content**.

<p align="center"><img width="517" alt="Select My Content." src="https://github.com/user-attachments/assets/2daadb3c-80fc-47b1-ace9-931e78ba95ac" /></p>

4. Click the **account icon** in the upper-right corner.

<p align="center"><img width="517" alt="Click the account icon in the upper-right corner." src="https://github.com/user-attachments/assets/a0a055e3-e9da-4280-bacc-7f7f65ca8f33" /></p>

5. If your personal account is not listed under **Recent accounts**, select **Add ArcGIS Online Account**.

<p align="center"><img width="317" alt="If your personal account is not listed under Recent accounts, select Add ArcGIS Online Account." src="https://github.com/user-attachments/assets/6cab6f8a-ae6f-430d-8d0d-cb617760bae6" /></p>

6. Sign in with your personal account. If you have a public account, use **ArcGIS login**.

<p align="center"><img width="317" alt="Sign in with your personal account. If you have a public account, use ArcGIS login." src="https://github.com/user-attachments/assets/c26cb1dc-d665-4802-b81b-f80133cc68f3" /></p>

#### **Copy Items to Your Personal Account**

This approach applies to CSV, Shapefile, GeoJSON, CSV Collection, web map, and StoryMap items. If the items are connected and used within one project, migrate them in dependency order. In the case of a StoryMap, copy the source data first, then the web map, and finally the StoryMap.

1. Make sure your institutional account is **active** and that you are logged in to ArcGIS Assistant.

<p align="center"><img width="317" alt="Make sure your institutional account is active and that you are logged in to ArcGIS Assistant." src="https://github.com/user-attachments/assets/85a4cfe2-b408-4362-8490-ad7918b938d5" /></p>

2. If another account is active, click the three dots next to your institutional account and select **Switch active account**.

<p align="center"><img width="317" alt="If another account is active, click the three dots next to your institutional account and select Switch active account." src="https://github.com/user-attachments/assets/0b5b865f-6cea-41f3-a736-711d47d0be6d" /></p>

3. Under **My Content**, locate the item you want to migrate.

<p align="center"><img width="517" alt="Under My Content, locate the item you want to migrate." src="https://github.com/user-attachments/assets/d0a9a19e-7bd1-4ca4-9bdd-801bd8a8fea4" /></p>

4. Check the **Title** and **Type**.

5. Select the **checkbox** beside the item.

<p align="center"><img width="517" alt="Select the checkbox beside the item." src="https://github.com/user-attachments/assets/01ad842a-13a7-4d41-a6a0-d0b1cbeceeb6" /></p>

6. Click **Copy Items**.

<p align="center"><img width="517" alt="Click Copy Items." src="https://github.com/user-attachments/assets/44814e8b-d551-42ee-a9e8-a918116be2bd" /></p>

7. Under **Copy Destination**, select your personal account.

<p align="center"><img width="317" alt="Under Copy Destination, select your personal account." src="https://github.com/user-attachments/assets/76556e5f-b8b7-4cf7-b256-8d038dabe166" /></p>

8. Click **Select Account**.

9. Select a folder and click **Select Folder**.

<p align="center"><img width="317" alt="Select a folder and click Select Folder." src="https://github.com/user-attachments/assets/206fd737-bdf4-4491-a924-33964cc7c8a7" /></p>

10. Check that the **Item Title** is correct.

<p align="center"><img width="317" alt="Check that the Item Title is correct." src="https://github.com/user-attachments/assets/792f308b-12da-4131-a7bc-d4743e9ed088" /></p>

11. Click **Copy Item**.

12. When the copy is complete, click **Open in ArcGIS Online**.

<p align="center"><img width="317" alt="When the copy is complete, click Open in ArcGIS Online." src="https://github.com/user-attachments/assets/fc0227ca-8fe9-4077-a216-56460fb563eb" /></p>

#### **Transfer Items That Cannot Be Copied Directly**

Some item types, such as feature services, hosted feature layers, feature layers, and media layers, **cannot** be copied as a complete item using ArcGIS Assistant. Instead, they can be copied as **a reference**, which means the copied item continues to use the original service in the institutional account. If the original service is deleted or access is removed, the copied item will **no longer work**. In this tutorial, we use a hosted feature layer as an example.

1. In ArcGIS Assistant under **My Content**, find the hosted layer. ArcGIS Assistant may show its **Type** as **Feature Service**.

<p align="center"><img width="517" alt="In ArcGIS Assistant under My Content, find the hosted layer. ArcGIS Assistant may show its Type as Feature Service." src="https://github.com/user-attachments/assets/cbf27d89-84b5-4105-a345-cf0a14f71bfd" /></p>

2. Select the checkbox beside the item and click **Copy Items**.

3. Under **Copy Destination**, select **your personal account**.

<p align="center"><img width="317" alt="Under Copy Destination, select your personal account." src="https://github.com/user-attachments/assets/c7f09b33-1201-4ce8-afc1-74f6e13baa6a" /></p>

4. Click **Select Account**.

5. Select a folder and click **Select Folder**.

<p align="center"><img width="317" alt="Select a folder and click Select Folder." src="https://github.com/user-attachments/assets/1e2a6add-7fae-455d-9c9f-2b80206da0aa" /></p>

6. Check that the **Item Title** is correct.

<p align="center"><img width="317" alt="Check that the Item Title is correct." src="https://github.com/user-attachments/assets/aa27be92-df12-4d77-b93c-4978e655010b" /></p>

7. Select **Copy by reference**.

<p align="center"><img width="317" alt="Select Copy by reference." src="https://github.com/user-attachments/assets/3fe44335-769d-445b-a8f0-f89b949b44c4" /></p>

8. Once everything is ready, click **Copy Item**.

9. When the copy is complete, click **Open in ArcGIS Online**.

<p align="center"><img width="317" alt="When the copy is complete, click Open in ArcGIS Online." src="https://github.com/user-attachments/assets/ef7edf0f-1785-41d8-b372-79c2ad551723" /></p>

*Note:* **Copy by reference** creates an item in the personal account, but the data and service remain in the institutional account. **Leave the URL unchanged** unless the same layer has been published at a new service URL.

### **After Transfer**

After the transfer, sign in to your personal account in [ArcGIS Online](https://www.arcgis.com/) and make sure the items were transferred correctly. After logging in, go to the **Content** tab and check that the transferred items and item types are correct.

#### **CSV Shapefile GeoJSON and CSV Collection**

1. **Open** each copied item.

2. For **CSV, Shapefile, and GeoJSON**, **confirm** that the file can be **downloaded**.

3. For a **CSV Collection**, **confirm** that its **tables and files** are available.

#### **Web Map**

1. **Open** the copied **Web Map**.

2. **Open** the map in **Map Viewer**.

3. **Open** the **Layers** panel.

4. **Confirm** that every layer displays correctly.

A Web Map stores map settings and links to its layers. A copied map may still use layers from the institutional account.

#### **StoryMap**

1. **Open** the copied **StoryMap**.

2. **Select View Story.**

3. **Check** the **text, images, maps, and other media**.

Web Maps, Web Scenes, hosted layers, embeds, and linked media are separate connected items. Confirm that each one opens correctly.

#### **Hosted Feature Layer**

1. **Open** the copied item.

2. **Confirm** that the **service URL** opens.

3. **Confirm** that the layer displays correctly.

#### **Final Check**

- **Each copied item** appears in the **correct folder**;

- **Item titles** are **clear**;

- **Files, maps, layers, and stories** open as expected.

### **Resources**

This tutorial focuses on transferring some common items in ArcGIS Online from an institutional account to a personal public account or other institution’s account. For help with other item types or more complex projects, use the following resources:

- [ArcGIS Assistant User Guide](https://guide.assistant.esri-ps.com/) for inspecting, copying, and modifying ArcGIS items;

- [ArcGIS Assistant Common Workflows](https://guide.assistant.esri-ps.com/docs/common-workflows) for copying StoryMaps and understanding referenced content;

- [Migrating Content Between ArcGIS Online Organizational Accounts](https://sites.psu.edu/psugis/software/migrating-agol-content/) by Penn State for an older ArcGIS Online Assistant workflow;

- [ArcGIS Online Account and Public Account FAQ](https://doc.arcgis.com/en/arcgis-online/reference/faq.htm) by Esri;

- [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;

- [ArcGIS Online Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online) for questions and shared solutions;

- [ArcGIS Assistant Feedback](https://github.com/EsriPS/arcgis-assistant-feedback) for reporting problems with the beta application.

If you have any questions about the tool or this tutorial, do not hesitate to contact the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)), for further support.
