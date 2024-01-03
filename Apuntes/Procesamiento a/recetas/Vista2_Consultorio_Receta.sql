create view RecyConsul as select c.id_consultorio as Dim_Consultorio, r.id_receta as Hecho_Receta 
from Hecho_Receta as r, Dim_Consultorio as c  
where c.id_consultorio=r.id_receta and c.id_consultorio= 1