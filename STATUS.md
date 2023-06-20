What has been done:
-Updated Code of oa-cache, oa-put, oa-get | helpers and sources folders


Status Dummy File:
python .\oa-get download-metadata pmc_doi | works with dois added in download_metadata function
python .\oa-get download-metadata dummy   | Download of test files works if file url is a direct link to the file
python .\oa-cache find-media dummy |  works by changing how dummy works
python .\oa-put upload-media dummy | doesnt work yet because it uses old elixir functions (.query) which have to be replaced with new ones

Elixir replacement has to be found especially for .query function
to-do: 
    - elixir equivalent
    - oa-cache convert-media ffmpeg config
    - sqllite server