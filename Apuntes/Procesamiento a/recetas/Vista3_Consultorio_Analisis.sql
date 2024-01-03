create view aliycons as select c.id_consultorio as Dim_Consultorio, a.di_analisis as Dim_Analisis 
from Dim_Analisis as a, Dim_Consultorio as c  
where c.id_consultorio=a.di_analisis and c.id_consultorio= 1