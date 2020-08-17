
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>VincentASR</title>
</head>
<body>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" enctype="multipart/form-data">
    <label for="file">文件名：</label>
    <input type="file" name="file" id="file"><br>
    <input type="submit" name="submit" value="提交">
</form>
<?php
$allowedExts = array("mp3", "m4a", "wav");
$temp = explode(".", $_FILES["file"]["name"]);
// echo $_FILES["file"]["size"];
$extension = end($temp);     // 获取文件后缀名
if ((
($_FILES["file"]["type"] == "audio/mpeg")
|| ($_FILES["file"]["type"] == "audio/mpeg-4")
|| ($_FILES["file"]["type"] == "audio/x-wav"))
&& ($_FILES["file"]["size"] < 102400000)   // 小于 10 Mb
&& in_array($extension, $allowedExts))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    }
    else
    {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
//         echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"] . "<br>";

        // 判断当前目录下的 upload 目录是否存在该文件
        // 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
        if (file_exists("upload/" . $_FILES["file"]["name"]))
        {
            echo $_FILES["file"]["name"] . " 文件已经存在。 ";
        }
        else
        {
            // 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
            move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);
            echo "文件存储在: " . "upload/" . $_FILES["file"]["name"];

            echo shell_exec('ls');
            echo shell_exec('./soxall.sh upload');
            echo shell_exec('./run.sh');

        }
    }
}

?>
</body>
</html>