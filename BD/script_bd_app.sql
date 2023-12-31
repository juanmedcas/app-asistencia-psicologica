USE [db_asistencia_psicologica]
GO
/****** Object:  User [user_db_aap]    Script Date: 12/10/2023 3:29:19 a. m. ******/
CREATE USER [user_db_aap] FOR LOGIN [user_db_aap] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_accessadmin] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_securityadmin] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_ddladmin] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_backupoperator] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_datareader] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_denydatareader] ADD MEMBER [user_db_aap]
GO
ALTER ROLE [db_denydatawriter] ADD MEMBER [user_db_aap]
GO
/****** Object:  Table [dbo].[Psicologo]    Script Date: 12/10/2023 3:29:19 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Psicologo](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Nombre] [varchar](40) NOT NULL,
	[Universidad] [varchar](40) NULL,
	[Email] [varchar](40) NULL,
	[Telefono] [int] NULL,
	[Titulo] [varchar](40) NULL,
	[Ciudad] [varchar](40) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Psicologo] ON 

INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (2, N'Claudia Cantor', N'La Salle', N'claucantor@gmail.com', 3671545, N'Profesional en Psocología', N'Bogotá D.C')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (3, N'Andres Gomez', N'Universidad del Bosque', N'psiandres@gmail.com', 3612032, N'Psocologo Profesional', N'Bogotá D.C')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (4, N'Pepito', N'Santo Tomas', N'pp@gmail.com', 3001020, N'Psicologo', N'Bogotá D.C')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (5, N'Pepit', N'Uni', N'df@gmail.com', 3000000, N'Psico', N'bogo')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (6, N'Pepit', N'Uni', N'df@gmail.com', 3000000, N'Psico', N'bogo')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (9, N'Pepito Perez', N'Javeriana', N'pepito@gmail.com', 3673434, N'Psicologo', N'Bogotá')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (10, N'Pepito Perez', N'Javeriana', N'pepito@gmail.com', 3673434, N'Psicologo', N'Bogotá')
INSERT [dbo].[Psicologo] ([Id], [Nombre], [Universidad], [Email], [Telefono], [Titulo], [Ciudad]) VALUES (11, N'Pepito Perez', N'Javeriana', N'pepito@gmail.com', 3673434, N'Psicologo', N'Bogotá')
SET IDENTITY_INSERT [dbo].[Psicologo] OFF
GO
