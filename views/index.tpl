%include header title='index@ '

<h1>= 任务追踪(Bottle版) =</h1>
<h2>== 待办 ==</h2>

<ol>
%for item in todolist:
  <li>{{item['txt']}}
  <sub></sub>
  <sup><a href="/hist/{{item['id']}}">历史</a>::<a href="/done/{{item['id']}}">完成</a>
    |<a href="/edit/{{item['id']}}">修改</a>
    |<a href="/dele/{{item['id']}}">删除</a></sup></li>
%end
</ol>

<h2>== 完成 ==</h2>
<ul>
%for item in donelist:
  <li><del>{{item['txt']}}</del>
  <sub></sub>
  <sup><a href="/hist/{{item['id']}}">历史</a>::<a href="/redo/{{item['id']}}">重启</a></sup>
  </li>
%end
</ul>

<h2>== 追加 ==</h2>
<form action="/add" method="POST">
<input type="text" name="txtadd" size="100" maxlength="280"/>
<button type="submit">就酱</button>
</form>


%include footer

