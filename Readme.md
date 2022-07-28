# Generate description from melt kdenlive

Get note from kdenlive and generate a file for description youtube

Generate a template for youtube 

```
{{Title}}
{{data one}}
{{Time and description}} # from note in kdenlive file
{{end of descriptio}}
```


## Usage

generate_description mi_file.kdenlive -c config

template config
```
[[title]]

[[timeslap]]

[[information]]

[[links]]
```