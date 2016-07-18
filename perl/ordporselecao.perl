
@teste=(1 .. 9999);
print "@teste\n"; #imprime desordenado!!!
&ordena;
print "@teste\n"; #imprime ordenado!!!!!

sub ordena
{
  $max=9999; #numero máximo de elementos!!!!
  for ($i=0; $i<=($max-1); $i++)
  {
    for ($j=0; $j<=$max; $j++)
    {
      
    if (@teste[$j] <= @teste[$i])
      {
        $aux=@teste[$i];
        @teste[$i]=@teste[$j];
        @teste[$j]=$aux;
     
    }
  }
}
}