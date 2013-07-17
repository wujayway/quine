q = 39
list = [
'   ',
'====Python====',
'q = 39',
'list = [',
']',
'for i in range(12,15):',
'    print list[i]',
'for i in list:',
'    print chr(q)+i+chr(q)+chr(44)',
'for i in range(15,23):',
'    print list[i]',
'====PHP====',
'<?php',
'$q = 39;',
'$list = array(',
');',
'for($i=2;$i<4;$i++)',
'  echo $list[$i].chr(10);',
'foreach($list as $i)',
'  echo chr($q).$i.chr($q).chr(44).chr(10);',
'for($i=4;$i<11;$i++)',
'  echo $list[$i].chr(10);',
'?>',
]
for i in range(12,15):
    print list[i]
for i in list:
    print chr(q)+i+chr(q)+chr(44)
for i in range(15,23):
    print list[i]
