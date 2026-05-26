# **Transferring Data to a Public ArcGIS Account**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: March 3, 2026*

This tutorial provides step-by-step guidance on how to transfer work on ArcGIS Online from a Duke institutional account to the free (aka ‘public’) version of the service.

To support the long-term preservation of ArcGIS projects for individuals who are no longer affiliated with the university, this tutorial is intended to assist DKU and Duke students, faculty, and staff in transferring and storing work in a personal (public) account.

[**Exporting Tools**](#exporting-tools)

[**Tool Limitations**](#tool-limitations)

[**Format Considerations**](#format-considerations)

[**Exporting Data from Item Page**](#exporting-data-from-item-page)

[**Exporting Data using Extra Data tool**](#exporting-data-using-extra-data-tool)

[**Uploading Data to Public Account**](#uploading-data-to-public-account)

[**Learning More**](#learning-more)

**Transferable Items**

To transfer data from an institutional ArcGIS Online account to a public (free) account, you can **only** export those layers that you own or that have export permissions enabled.

More complex items (e.g. web maps, StoryMaps) **cannot be exported in full**. To transfer these, you will need to manually download the individual assets (e.g., spatial layers, images, audio files) and recreate the item in your public account.

Note that certain ArcGIS applications (e.g. Experience Builder, Dashboards, Survey123) are **not** supported in public accounts.

### **Exporting Tools** 

We will cover two exporting tools in this tutorial: *Export Data* function on an individual item’s Details page and the *Extract Data* tool.

Export Data is a feature on the Item Details page in ArcGIS Online that allows users to export data in various formats, including Shapefile, CSV, KML, Excel, File Geodatabase (FGDB), GeoJSON, and GeoPackage. Only hosted feature layers can be exported. To learn more about the definition, see [feature layers](https://doc.arcgis.com/en/arcgis-online/reference/feature-layers.htm). For detailed instructions, see [ArcGIS Online: Export data from hosted feature layers](https://doc.arcgis.com/en/arcgis-online/manage-data/use-hosted-layers.htm#GUID-47A1D795-B330-45D7-89F7-9203A99E6924).

Extract Data tool is a geoprocessing tool in ArcGIS Online that packages feature layers and tables into formats such as CSV, File Geodatabase (.zip), Shapefile (.zip), and KML. This tool creates an item within your content that contains the data from the selected layers. You can download the data directly from the item. While powerful, the tool is applicable to layers that can be opened in Map Viewer. For detailed information on limitations, see the documentation [here](https://doc.arcgis.com/en/arcgis-online/analyze/extract-data-mv.htm).

### **Tool Limitations** 

Exported files may take some time to process and might not be fully restorable in a public ArcGIS Online account. For the tools covered in this tutorial, please note the following common limitations:

* The time to export data from ArcGIS Online varies significantly depending on the size of the dataset, the internet connection, and the chosen export format. It can take anywhere from a few minutes to several hours, or even longer for large datasets.  
* Some specialized layer types (e.g., raster layers, time-enabled layers, or certain 3D layers) may not be compatible with both tools.

### **Format Considerations**

While ArcGIS Online supports a variety of export formats, public accounts only support uploading files in CSV, KML, and GeoJSON formats. When transferring data to a public ArcGIS Online account, it is important to understand the limitations of each supported file format:

* GeoJSON: Full feature properties (such as symbology and styles) may not be preserved during export/import. To maintain the same visual representation in the new map project, manual adjustments will be required after import.  
* KML: While visible features are generally preserved, KML offers limited post-import editing capabilities. For example, you will not be able to adjust styles or configure pop-ups within ArcGIS Online after the import.  
* CSV: Only non-spatial attributes are retained unless the file includes latitude and longitude columns. Without spatial data, the CSV file cannot be imported as a spatial layer into a new map project.

### **Exporting Data from Item Page** 

1\. Log in to [ArcGIS Online](https://www.arcgis.com/sharing/oauth2/authorize?client_id=arcgisonline&response_type=code&state=%7B%22portalUrl%22%3A%22https%3A%2F%2Fwww.arcgis.com%22%2C%22uid%22%3A%22Eae4_LWCvrMN4HneelAeKdOsBBEPtvoRlAZMJG33ecw%22%2C%22useLandingPage%22%3Atrue%2C%22clientId%22%3A%22arcgisonline%22%7D&expiration=20160&locale=en-us&redirect_uri=https%3A%2F%2Fwww.arcgis.com%2Fhome%2Faccountswitcher-callback.html&force_login=true&redirectToUserOrgUrl=true&code_challenge=G5qu2wdtERhd8NB7wWeVriyIZeRVm6Aqu1YTsKbDJ64&code_challenge_method=S256&display=default&hideCancel=true&showSignupOption=true&canHandleCrossOrgSignIn=true&signuptype=esri&allow_verification=true) using organization’s URL and NetID account (see instructions [here](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/Signing%20In%20to%20ArcGIS.md)).

2\. Go to **Content** tab, navigate and click on the item in **Feature layer (hosted)** format.

<p align="center"><img width="317"  alt="1" src="https://github.com/user-attachments/assets/82ec6d31-264d-4f25-952f-3404bfa7f0df" />


3\. On the layer's item details page, under the **Overview** tab, click **Export Data**, then **Export to GeoJSON**.

<p align="center"><img width="317"  alt="2" src="https://github.com/user-attachments/assets/f83d16a3-c0c5-4107-af56-f1f391dcb30c" />


4\. Enter a title for the new file and add any other information. Then, click **Export**.

<p align="center"><img width="317" alt="3" src="https://github.com/user-attachments/assets/ddf4409f-5f5a-4246-a007-d0bcacfc5c09" />



5\. A new item page will open. On the **Overview** tab, click **Download** to save the file in the local computer.

<p align="center"><img width="317" alt="4" src="https://github.com/user-attachments/assets/199f22fe-054b-400b-b892-baa4ec9046a0" />


### **Exporting Data using Extra Data tool**

1\. Go to **Content** tab, navigate and click on a map item to start.

2\. Click **Open in Map Viewer**. 

3\. In the menu in the toolbar on the right, click **Analysis** icon, select **Extract Data** under **Manage data**.

<p align="center"><img width="317"  alt="5" src="https://github.com/user-attachments/assets/d6527992-a512-4b74-aeab-9ee250679dd1" />



4\. For **Input layer**, select the desired layer or layers. You can choose multiple layers here.

5\. For **Result layer**, specify the output data format, output name, and location.

<p align="center"><img width="317" alt="6" src="https://github.com/user-attachments/assets/f66516de-b974-4d8b-a51f-464f6ea4eca1" />



6\. Click **Estimate Credits** to check if you have enough credits. To view your remaining credits, click your profile in the top right corner, go to **My Settings**, and then select **Credits**. If you don’t have enough credits to run the tool, please contact the DKU library.

7\. Make sure you have enough credits, and click **Run**.

8\. Go to **History** tab to check the processing statues and output.

<p align="center"><img width="517" alt="7" src="https://github.com/user-attachments/assets/3ff89dcd-7a69-4fac-85ca-8db9d99f8711" />



9\. Once the task is completed, click on the task record. In the open tab, click the three-dot icon and select **Open Item details**.

<p align="center"><img width="517"  alt="8" src="https://github.com/user-attachments/assets/89ec898d-db69-47e1-a3d8-4332cbcc3d95" />



10\. A new item page will open. On the **Overview** tab, click **Download** to save the file in the local computer.

<p align="center"><img width="317"  alt="9" src="https://github.com/user-attachments/assets/b164bd03-0f56-4eea-b28f-096f4f6d2a65" />



### **Uploading Data to Public Account**

1\. If you don’t have an ArcGIS Online public account, use this [link](https://www.arcgis.com/sharing/rest/oauth2/signup?client_id=arcgisonline&redirect_uri=http://www.arcgis.com&response_type=token) to create one.

2\. Log in to your [ArcGIS Online public account](https://www.arcgis.com/sharing/oauth2/authorize?client_id=arcgisonline&response_type=code&state=%7B%22portalUrl%22%3A%22https%3A%2F%2Fwww.arcgis.com%22%2C%22uid%22%3A%22Eae4_LWCvrMN4HneelAeKdOsBBEPtvoRlAZMJG33ecw%22%2C%22useLandingPage%22%3Atrue%2C%22clientId%22%3A%22arcgisonline%22%7D&expiration=20160&locale=en-us&redirect_uri=https%3A%2F%2Fwww.arcgis.com%2Fhome%2Faccountswitcher-callback.html&force_login=true&redirectToUserOrgUrl=true&code_challenge=G5qu2wdtERhd8NB7wWeVriyIZeRVm6Aqu1YTsKbDJ64&code_challenge_method=S256&display=default&hideCancel=true&showSignupOption=true&canHandleCrossOrgSignIn=true&signuptype=esri&allow_verification=true) using your ArcGIS login credentials.

<p align="center"><img width="317"  alt="10" src="https://github.com/user-attachments/assets/9945a5bc-f9ab-4cca-a579-01b8b44477b2" />

3\. Click on the **Map** tab to open the **Map Viewer**.

<p align="center"><img width="517" alt="11" src="https://github.com/user-attachments/assets/b0e4630a-de33-4739-b10a-27232aeccd68" />


4\. Click **Add** from the left menu, select **Add layer from file**.

<p align="center"><img width="517"  alt="12" src="https://github.com/user-attachments/assets/44228c67-ce70-4022-b188-1203feab32bb" />



5\. Choose the file from your device, click **Open**, click **Create and add to map**.

<p align="center"><img width="517" alt="13" src="https://github.com/user-attachments/assets/93f88e89-d29d-4694-83d4-055d8b46e567" />



6\. From the left menu, click **Save and open**, then **Save as**.

<p align="center"><img width="517"  alt="14" src="https://github.com/user-attachments/assets/4a4cbfc2-b681-4ed3-a622-44312be9eed6" />



7\. Fill out the title and click **Save**.

<p align="center"><img width="517" height="538" alt="15" src="https://github.com/user-attachments/assets/d5084484-114f-4de0-b3a8-62923198877a" />



8\. The project is now successfully transferred and saved in your ArcGIS Online public account.

### **Learning More**

If you are interested in learning more about preserving GIS projects, transferring data from ArcGIS Online, or continuing your mapping projects using free GIS tools, consider exploring the following resources:

* [DKU Library’s GIS guide](https://library.dukekunshan.edu.cn/geographic-information-system-gis/) provides information on [QGIS](https://qgis.org/) and [Mapbox](https://www.mapbox.com/), two free and open-source GIS platforms accessible to all users.  
* You can [download publicly shared data in shapefile format](https://support.esri.com/en-us/knowledge-base/how-to-download-publicly-shared-data-from-arcgis-online-000015899) from ArcGIS Online to your local machine for use in other GIS platforms.  
* If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei (siti.lei@dukekunshan.edu.cn) for further support.
