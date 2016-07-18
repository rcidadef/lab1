#!/bin/perl
#para uma busca binaria é necessario que o vetor esteja ordenado!!!!
@vetor = (1 .. 999999);
$x=0; #$x será o elemento à procurar.
$inicio=0;
$fim=@vetor; # $fim recebe o tamanho de @vetor.
$meio=int(($inicio+$fim)/2);
print "Procurando $x em ". "@vetor". "\n";
while (($x != @vetor[$meio]) && ($inicio!=$fim) && ($inicio<$fim))
           {
             if ($x > @vetor[$meio]) {$inicio=$meio+1}
             else {$fim=$meio-1}
             $meio=int(($inicio+$fim)/2);
           }
if ($x == @vetor[$meio]){print "$x encontrado em @". "vetor[". $meio. "]\n";}
else {print "$x nao encontrado!! \n";}
