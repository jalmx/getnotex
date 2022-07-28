# Got note from kdenlive

Get note from kdenlive and generate a file for description youtube


## How to use

```
 Script to get note from file kdenlive a youtube time format
    
    HOW TO USE:
    
        getnotex file.kdenlive 
```

### Result 

**From**

```xml
<property name="kdenlive:documentnotes">&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">
p, li { white-space: pre-wrap; }
&lt;/style>&lt;/head>&lt;body style=" font-family:'Roboto'; font-size:10pt; font-weight:400; font-style:normal;">
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Al inicio&lt;/p>
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;a href="0">&lt;span style=" text-decoration: underline; color:#2980b9;">00:00:00,00&lt;/span>&lt;/a> Inicio de la clase 00:00&lt;/p>
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;a href="3576">&lt;span style=" text-decoration: underline; color:#2980b9;">00:01:59,08&lt;/span>&lt;/a> Segundo comentario 01:59&lt;/p>
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;a href="20153">&lt;span style=" text-decoration: underline; color:#2980b9;">00:11:12,13&lt;/span>&lt;/a> Otro comentario a los 11:12&lt;/p>
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;a href="26862">&lt;span style=" text-decoration: underline; color:#2980b9;">00:14:56,08&lt;/span>&lt;/a> [Referencia] a otro video 14:56&lt;/p>
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;a href="29508">&lt;span style=" text-decoration: underline; color:#2980b9;">00:16:24,18&lt;/span>&lt;/a> El ultimo punto 16:24&lt;/p>
&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Texto sin refencia&lt;/p>&lt;/body>&lt;/html></property>
```

**To**

```markdown
Al inicio
00:00 Inicio de la clase 00:00
01:59 Segundo comentario 01:59
11:12 Otro comentario a los 11:12
14:56 [Referencia] a otro video 14:56
16:24 El ultimo punto 16:24
Texto sin refencia
```

## How to install

- Download [script](https://raw.githubusercontent.com/jalmx/generate_description_from_kdenlive_to_yt/master/bin/getnotex) to save `getnotex`
- change permission with `sudo chmod +x getnotex`
- Copy to PATH
- Or use `python getnotex`

## Requirements

- `BeautifulSoup`