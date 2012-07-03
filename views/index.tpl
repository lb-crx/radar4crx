%include header title='index@ '

<h1>= 雷达图生成器(Bottle版) =</h1>
基于: <a href="http://bbs.liebao.cn/thread-16619-1-1.html">爱猎豹爱扩展~猎豹兼容扩展推荐活动开始啦！[v12.6.13]</a>

<h2>== 评分 ==</h2>

<form action="/radar" method="POST">

<table id="optradios">
    <tr class="title">
        <td>
象限\分数
        </td>
        <td>
1
        </td>
        <td>
2
        </td>
        <td>
3
        </td>
        <td>
4
        </td>
        <td>
5
        </td>
    </tr>
    
    <tr>
        <td>
<b>易用:</b>
        </td>
        <td>
<input type="radio" name="easy" value="1">
        </td>
        <td>
<input type="radio" name="easy" value="2">
        </td>
        <td>
<input type="radio" name="easy" value="3" checked="true">
        </td>
        <td>
<input type="radio" name="easy" value="4">
        </td>
        <td>
<input type="radio" name="easy" value="5">
        </td>
    </tr>
    
    <tr>
        <td>
<b>功能:</b>
        </td>
        <td>
<input type="radio" name="func" value="1">
        </td>
        <td>
<input type="radio" name="func" value="2">
        </td>
        <td>
<input type="radio" name="func" value="3" checked="true">
        </td>
        <td>
<input type="radio" name="func" value="4">
        </td>
        <td>
<input type="radio" name="func" value="5">
        </td>
    </tr>

    <tr>
        <td>
<b>活跃:</b>
        </td>
        <td>
<input type="radio" name="acti" value="1">
        </td>
        <td>
<input type="radio" name="acti" value="2">
        </td>
        <td>
<input type="radio" name="acti" value="3" checked="true">
        </td>
        <td>
<input type="radio" name="acti" value="4">
        </td>
        <td>
<input type="radio" name="acti" value="5">
        </td>
    </tr>

    <tr>
        <td>
<b>美观:</b>
        </td>
        <td>
<input type="radio" name="beau" value="1">
        </td>
        <td>
<input type="radio" name="beau" value="2">
        </td>
        <td>
<input type="radio" name="beau" value="3" checked="true">
        </td>
        <td>
<input type="radio" name="beau" value="4">
        </td>
        <td>
<input type="radio" name="beau" value="5">
        </td>
    </tr>
</table>

<button type="submit">就酱</button>
</form>


%include footer

