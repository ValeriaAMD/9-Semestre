create view RecyAnalisis as select a.Tipo as Dim_Analisis, m.medicamento as Hecho_Receta 
from Hecho_Receta as m, Dim_Analisis as a  
where a.Tipo=m.medicamento and a.Tipo= 'semen'