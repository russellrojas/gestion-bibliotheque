INSERT INTO biblio.Ressource (codeRessource, titre, dateApparition, editeur, genre, codeClassification)
VALUES
-- 10 pour Livre
('R001', 'Le Dernier Livre', '2024-11-12', 'Éditions XYZ', 'Fiction', '001'),
('R002', 'Voyage au Bout du Monde', '2023-05-22', 'Éditions ABC', 'Aventure', '002'),
('R003', 'L''Histoire de la Musique', '2020-09-10', 'Éditions Musica', 'Musique', '003'),
('R004', 'La Cuisine Française', '2021-01-15', 'Éditions Gourmet', 'Culinaire', '004'),
('R005', 'Les Secrets de l''Espace', '2022-08-18', 'Éditions Cosmos', 'Science', '005'),
('R006', 'Le Pouvoir du Marketing', '2023-11-03', 'Éditions Business', 'Affaires', '006'),
('R007', 'Les Mystères de l''Histoire', '2019-06-05', 'Éditions Histoire', 'Historique', '007'),
('R008', 'Les Voyages Imaginaires', '2020-03-12', 'Éditions Aventure', 'Science-fiction', '008'),
('R009', 'La Terre et Ses Secrets', '2022-10-22', 'Éditions Nature', 'Environnement', '009'),
('R010', 'Psychologie et Comportement', '2021-07-29', 'Éditions Psyché', 'Psychologie', '010'),

-- 10 pour Film
('R011', 'Film Aventure', '2021-12-10', 'Éditions Cinéma', 'Aventure', '011'),
('R012', 'Film Science-fiction', '2020-06-25', 'Éditions Cinéma', 'Science-fiction', '012'),
('R013', 'Le Mystère du Temps', '2019-07-15', 'Éditions Cinéma', 'Science', '013'),
('R014', 'Les Enigmes de l''Histoire', '2022-09-18', 'Éditions Cinéma', 'Historique', '014'),
('R015', 'L''Art de la Cuisine', '2023-03-21', 'Éditions Cinéma', 'Culinaire', '015'),
('R016', 'Le Dernier Combat', '2021-05-30', 'Éditions Cinéma', 'Action', '016'),
('R017', 'Les Voyages Impossibles', '2020-11-10', 'Éditions Cinéma', 'Aventure', '017'),
('R018', 'Les Secrets de l''Univers', '2022-12-20', 'Éditions Cinéma', 'Science-fiction', '018'),
('R019', 'L''Invasion Extraterrestre', '2021-08-12', 'Éditions Cinéma', 'Science-fiction', '019'),
('R020', 'Le Mystère de la Terre', '2023-01-19', 'Éditions Cinéma', 'Science', '020'),

-- 10 pour OeuvreMusicale
('R021', 'Symphonie No. 1', '2020-05-15', 'Éditions Musique', 'Classique', '021'),
('R022', 'Voyage Musical', '2021-09-11', 'Éditions Musique', 'Jazz', '022'),
('R023', 'Les Grands Compositeurs', '2022-06-02', 'Éditions Musique', 'Classique', '023'),
('R024', 'Rythmes du Monde', '2021-11-25', 'Éditions Musique', 'World', '024'),
('R025', 'La Musique et l''Emotion', '2023-03-30', 'Éditions Musique', 'Classique', '025'),
('R026', 'Rhapsodie en Bleu', '2020-12-10', 'Éditions Musique', 'Jazz', '026'),
('R027', 'Symphonie des Âmes', '2021-07-20', 'Éditions Musique', 'Classique', '027'),
('R028', 'Concert des Légendes', '2022-08-14', 'Éditions Musique', 'Pop', '028'),
('R029', 'Musique Contemporaine', '2023-04-10', 'Éditions Musique', 'Classique', '029'),
('R030', 'Le Chant du Monde', '2021-10-18', 'Éditions Musique', 'World', '030');

-- table Livre
INSERT INTO biblio.Livre (codeRessource, isbn, resume, langue)
VALUES
('R001', '978-3-16-148410-0', 'Un récit fascinant qui explore les mystères du dernier livre.', 'Français'),
('R002', '978-1-4028-9462-6', 'Un voyage épique à travers les coins du monde, avec des personnages inoubliables.', 'Français'),
('R003', '978-0-307-29136-2', 'Une analyse approfondie de l''évolution de la musique à travers les âges.', 'Français'),
('R004', '978-2-226-27483-3', 'Découvrez les secrets de la cuisine française avec des recettes traditionnelles.', 'Français'),
('R005', '978-2-321-45368-7', 'Plongée dans l''univers fascinant de l''espace et des découvertes scientifiques récentes.', 'Français'),
('R006', '978-0-06-247261-1', 'L''importance du marketing dans le monde moderne et ses secrets de succès.', 'Français'),
('R007', '978-0-06-211793-7', 'Les mystères cachés dans l''histoire de l''humanité, du passé à aujourd''hui.', 'Français'),
('R008', '978-1-250-07435-7', 'Voyagez dans des mondes imaginaires avec cette œuvre de science-fiction passionnante.', 'Français'),
('R009', '978-1-4000-3375-7', 'Une exploration détaillée des phénomènes naturels qui façonnent notre planète.', 'Français'),
('R010', '978-0-14-312773-0', 'Une étude sur la psychologie humaine et ses comportements en société.', 'Français');

-- table Film
INSERT INTO biblio.Film (codeRessource, longueur, langue, synopsis)
VALUES
('R011', 120, 'Français', 'Un thriller captivant qui suit un détective dans une course contre la montre pour résoudre une affaire mystérieuse.'),
('R012', 150, 'Français', 'Un voyage épique autour du monde avec une équipe de scientifiques explorant des mystères antiques.'),
('R013', 130, 'Français', 'Un documentaire approfondi sur l''évolution de la musique, de ses débuts à aujourd''hui.'),
('R014', 100, 'Français', 'Une aventure culinaire à travers les traditions de la cuisine française, avec des chefs renommés.'),
('R015', 140, 'Français', 'Un voyage à travers l''espace et les découvertes qui changent notre compréhension de l''univers.'),
('R016', 110, 'Français', 'Un film sur l''impact du marketing dans le monde moderne et la manière dont il influence nos décisions.'),
('R017', 160, 'Français', 'Les mystères cachés dans l''histoire de l''humanité, du passé à aujourd''hui.'),
('R018', 180, 'Français', 'Une aventure dans des mondes imaginaires, explorant des possibilités infinies de l''espace et du temps.'),
('R019', 125, 'Français', 'Un film documentaire qui explore les phénomènes naturels et leurs effets sur la planète.'),
('R020', 135, 'Français', 'Un film explorant les aspects de la psychologie humaine et les comportements sociaux.');

INSERT INTO biblio.OeuvreMusicale (codeRessource, longueur)
VALUES 
('R021', 60),  -- durée en minutes
('R022', 70),
('R023', 65),
('R024', 80),
('R025', 90),
('R026', 75),
('R027', 85),
('R028', 95),
('R029', 110),
('R030', 120);

-- Table Exemplaire
INSERT INTO biblio.Exemplaire (etat, ressource) 
VALUES
('neuf', 'R001'),
('bon', 'R002'),
('abime', 'R003'),
('perdu', 'R004'),
('neuf', 'R005'),
('bon', 'R006'),
('abime', 'R007'),
('perdu', 'R008'),
('neuf', 'R009'),
('bon', 'R010'),
('neuf', 'R011'),
('bon', 'R012'),
('abime', 'R013'),
('perdu', 'R014'),
('neuf', 'R015'),
('bon', 'R016'),
('abime', 'R017'),
('perdu', 'R018'),
('neuf', 'R019'),
('bon', 'R020'),
('neuf', 'R021'),
('bon', 'R022'),
('abime', 'R023'),
('perdu', 'R024'),
('neuf', 'R025'),
('bon', 'R026'),
('abime', 'R027'),
('perdu', 'R028'),
('neuf', 'R029'),
('bon', 'R030');

-- table CompteUtilisateur
INSERT INTO biblio.CompteUtilisateur (login, motDePasse, role)
VALUES
('user1', 'password', 'adhérent'),
('user2', 'password', 'adhérent'),
('user3', 'password', 'adhérent'),
('user4', 'password', 'adhérent'),
('user5', 'password', 'adhérent'),
('user6', 'password', 'adhérent'),
('user7', 'password', 'adhérent'),
('user8', 'password', 'adhérent'),
('user9', 'password', 'adhérent'),
('user10', 'password', 'adhérent'),
('admin1', 'password', 'personnel'),
('admin2', 'password', 'personnel'),
('admin3', 'password', 'personnel'),
('admin4', 'password', 'personnel'),
('admin5', 'password', 'personnel'),
('admin6', 'password', 'personnel'),
('admin7', 'password', 'personnel'),
('admin8', 'password', 'personnel'),
('admin9', 'password', 'personnel'),
('admin10', 'password', 'personnel');


-- Insertion des données dans la table Adherent
INSERT INTO biblio.Adherent (informationsAdherent, adherentActuel, blacklister, compteUtilisateur)
VALUES
    ('{"nom": "Dupont", "prenom": "Jean", "dateNaissance": "1980-05-15", "adresse": "10 rue de Paris, 75001 Paris", "email": "jean.dupont@email.com", "numeroTel": "0123456789"}', TRUE, FALSE, 'user1'), 
    ('{"nom": "Martin", "prenom": "Claire", "dateNaissance": "1992-08-20", "adresse": "5 avenue des Champs, 75008 Paris", "email": "claire.martin@email.com", "numeroTel": "0123456790"}', TRUE, FALSE, 'user2'), 
    ('{"nom": "Bernard", "prenom": "Paul", "dateNaissance": "1975-02-10", "adresse": "12 boulevard Saint-Germain, 75005 Paris", "email": "paul.bernard@email.com", "numeroTel": "0123456791"}', TRUE, FALSE, 'user3'), 
    ('{"nom": "Lemoine", "prenom": "Sophie", "dateNaissance": "1988-11-25", "adresse": "30 rue de la République, 69001 Lyon", "email": "sophie.lemoine@email.com", "numeroTel": "0123456792"}', TRUE, FALSE, 'user4'), 
    ('{"nom": "Durand", "prenom": "Michel", "dateNaissance": "1965-09-12", "adresse": "18 rue de l''Italie, 75013 Paris", "email": "michel.durand@email.com", "numeroTel": "0123456793"}', TRUE, TRUE, 'user5'), 
    ('{"nom": "Moreau", "prenom": "Chloé", "dateNaissance": "1995-07-30", "adresse": "23 rue de la Liberté, 33000 Bordeaux", "email": "chloe.moreau@email.com", "numeroTel": "0123456794"}', TRUE, FALSE, 'user6'), 
    ('{"nom": "Girard", "prenom": "Luc", "dateNaissance": "1983-03-05", "adresse": "11 rue de Nantes, 44000 Nantes", "email": "luc.girard@email.com", "numeroTel": "0123456795"}', FALSE, FALSE, 'user7'), 
    ('{"nom": "Rouge", "prenom": "Isabelle", "dateNaissance": "1990-04-17", "adresse": "7 rue de l''Église, 21000 Dijon", "email": "isabelle.rouge@email.com", "numeroTel": "0123456796"}', TRUE, FALSE, 'user8'), 
    ('{"nom": "Giraud", "prenom": "Antoine", "dateNaissance": "1980-10-01", "adresse": "15 rue des Alpes, 06000 Nice", "email": "antoine.giraud@email.com", "numeroTel": "0123456797"}', TRUE, TRUE, 'user9'), 
    ('{"nom": "Leclerc", "prenom": "Nathalie", "dateNaissance": "1978-12-09", "adresse": "2 place de la Concorde, 75008 Paris", "email": "nathalie.leclerc@email.com", "numeroTel": "0123456798"}', TRUE, FALSE, 'user10');


-- table Personnel
INSERT INTO biblio.Personnel (nom, prenom, adresse, email, compteUtilisateur)
VALUES
('Dupont', 'Claude', '10 Rue de Paris, Paris, France', 'jean.dupont@email.com', 'admin1'),
('Martin', 'Marie', '12 Rue des Champs, Lyon, France', 'marie.martin@email.com', 'admin2'),
('Lemoine', 'Paul', '22 Boulevard des Lilas, Marseille, France', 'paul.lemoine@email.com', 'admin3'),
('Lefevre', 'Isabelle', '5 Avenue des Alpes, Toulouse, France', 'isabelle.lefevre@email.com', 'admin4'),
('Roux', 'Pierre', '14 Rue de la République, Lille, France', 'pierre.roux@email.com', 'admin5'),
('Berger', 'Sophie', '30 Rue de la Liberté, Nantes, France', 'sophie.berger@email.com', 'admin6'),
('Garnier', 'Thierry', '40 Rue du Centre, Bordeaux, France', 'thierry.garnier@email.com', 'admin7'),
('Benoit', 'Catherine', '8 Place du Marché, Nice, France', 'catherine.benoit@email.com', 'admin8'),
('Girard', 'Alain', '50 Rue de l''Église, Grenoble, France', 'alain.girard@email.com', 'admin9'),
('Perrot', 'Lucie', '100 Rue de la Paix, Paris, France', 'lucie.perrot@email.com', 'admin10');


-- table Pret
INSERT INTO biblio.Pret (datePret, dateRendu, adherent, exemplaire)
VALUES
('2024-11-15', '2024-12-05', 1, 1),  
('2024-11-18', '2024-12-25', 2, 5),
('2024-11-22', '2024-12-30', 3, 6),
('2024-11-25', '2025-01-05', 4, 4);


-- Prêts complétés
INSERT INTO biblio.Pret (datePret, dateRendu, statut, adherent, exemplaire)
VALUES 
('2024-01-10', '2024-01-20', 'rendu', 6, 20),
('2024-02-01', '2024-02-15', 'rendu', 8, 19),
('2024-03-05', '2024-03-20', 'rendu', 10, 25),
('2024-04-15', '2024-04-30', 'rendu', 9, 16);

-- table Suspension
INSERT INTO biblio.Suspension (adherent, dateSuspension, cause, dureeSuspension)
VALUES
(1, '2024-01-15', 'Retard dans la restitution', 30),  
(3, '2024-01-25', 'Non-respect des règles', 60),      
(5, '2024-02-05','Comportement inapproprié', 45),    
(7, '2024-02-10','Retard dans la restitution', 25);


-- table Contributeur
INSERT INTO biblio.Contributeur (nom, prenom, dateNaissance, nationalite)
VALUES
('Dupont', 'Pierre', '1980-05-15', 'Française'), 
('Martin', 'Sophie', '1992-07-20', 'Française'), 
('Lemoine', 'Julien', '1975-03-10', 'Belge'),    
('Durand', 'Lucie', '1989-09-25', 'Française'),  
('Lemoine', 'Mathieu', '1990-12-05', 'Belge'),   
('Lefevre', 'Amandine', '1983-11-18', 'Française'),
('Muller', 'Jean', '1978-02-25', 'Allemande'),  
('Pires', 'Antonio', '1995-06-30', 'Portugaise'), 
('Smith', 'Olivia', '1992-01-22', 'Anglaise'), 
('Fernandez', 'Carlos', '1985-04-10', 'Espagnole'); 

-- Table Auteur
INSERT INTO biblio.Auteur (livre, contributeur)
VALUES
('R001', 1),
('R002', 2),
('R003', 3),
('R004', 4),
('R005', 5),
('R006', 6),
('R007', 7),
('R008', 8),
('R009', 9),
('R010', 10);

-- Table Compositeur
INSERT INTO biblio.Compositeur (oeuvreMusicale, contributeur)
VALUES
('R021', 1),
('R022', 2),
('R023', 3),
('R024', 4),
('R025', 5),
('R026', 6),
('R027', 7),
('R028', 8),
('R029', 9),
('R030', 10);

-- Table Interprete
INSERT INTO biblio.Interprete (oeuvreMusicale, contributeur)
VALUES
('R021', 1),
('R022', 2),
('R023', 3),
('R024', 4),
('R025', 5),
('R026', 6),
('R027', 7),
('R028', 8),
('R029', 9),
('R030', 10);

-- Table Realisateur
INSERT INTO biblio.Realisateur (film, contributeur)
VALUES
('R011', 1),
('R012', 2),
('R013', 3),
('R014', 4),
('R015', 5),
('R016', 6),
('R017', 7),
('R018', 8),
('R019', 9),
('R020', 10);

-- Table Acteur
INSERT INTO biblio.Acteur (film, contributeur)
VALUES
('R011', 1),
('R012', 2),
('R013', 3),
('R014', 4),
('R015', 5),
('R016', 6),
('R017', 7),
('R018', 8),
('R019', 9),
('R020', 10);
