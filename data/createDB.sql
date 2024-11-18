CREATE TABLE IF NOT EXISTS Departements (
    code_departement TEXT,
    nom_departement TEXT,
    code_region INTEGER,
    zone_climatique TEXT,
    constraint pk_departements primary key (code_departement),
    constraint fk_region foreign key (code_region) references Regions(code_region)
);

CREATE TABLE IF NOT EXISTS Regions (
    code_region INTEGER,
    nom_region TEXT,
    constraint pk_regions primary key (code_region)
);

CREATE TABLE IF NOT EXISTS Mesures (
    code_departement TEXT,
    date_mesure DATE,
    temperature_min_mesure FLOAT,
    temperature_max_mesure FLOAT,
    temperature_moy_mesure FLOAT,
    constraint pk_mesures primary key (code_departement, date_mesure),
    constraint fk_mesures foreign key (code_departement) references Departements(code_departement)
);

CREATE TABLE IF NOT EXISTS Communes (
    code_commune INTEGER,
    code_departement TXT,
    nom_commune TEXT,
    statut_commune TEXT,
    altitude_moyenne INTEGER,
    population INTEGER,
    superficie INTEGER,
    code_canton INTEGER,
    code_arrondissemnt INTEGER,
    constraint pk_communes primary key (code_commune, code_departement),
    constraint fk_communes_departements foreign key (code_departement) references Departements(code_departement)
);



--TODO Q4 Ajouter les créations des nouvelles tables

-- Table: TypeTravaux Enumeration

-- CREATE TYPE Type_panneaux AS ENUM ('MONOCRISTALLIN', 'POLYCRISTALLIN');
-- CREATE TYPE Type_chaudiere AS ENUM ('STANDARD', 'AIR-EUA', 'a CONDENSATION', 'AUTRES', 'AIR-AIR', 'GEOTHERMIE', 'HPE' );
-- CREATE TYPE TypeGenerateur AS ENUM ('AUTRES', 'CHAUDIERE', 'INSERT', 'PAC', 'POELE', 'RADIATEUR');
-- CREATE TYPE TypeEnergie AS ENUM ('AUTRES', 'BOIS', 'ELECTRICITE', 'FIOUL', 'GAZ');
-- CREATE TYPE TypeIsolant AS ENUM ('AUTRES', 'PLASTIQUES', 'LAINE VEGETALE', 'LAINE MINIRALE');
-- CREATE TYPE TypePoste AS ENUM ('COMBLES PERDUES', 'ITI', 'ITE', 'RAMPANTS', 'SARKING', 'TOITURE TERRASSE', 'PLANCHER BAS');


-- Table: Travaux_Renovations
CREATE TABLE IF NOT EXISTS Travaux (
    id_renovation INTEGER PRIMARY KEY AUTOINCREMENT,
    code_departement TEXT,
    code_region INTEGER,
    cout_total_ht REAL,
    cout_induit_ht REAL,
    annee_travaux INTEGER,
    type_logement TEXT ,
    annee_construction_logement INT,
    CONSTRAINT fk_Travaux_region FOREIGN KEY (code_region) REFERENCES Regions(code_region),
    CONSTRAINT fk_Travaux_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement)
);

CREATE TABLE IF NOT EXISTS Isolations (
    id_travaux  PRIMARY KEY,
    poste TEXT CHECK (poste IN ('COMBLES PERDUES', 'ITI', 'ITE', 'RAMPANTS', 'SARKING', 'TOITURE TERRASSE', 'PLANCHER BAS','null')),
    isolant TEXT CHECK(isolant IN ('AUTRES', 'PLASTIQUES', 'LAINE VEGETALE', 'LAINE MINERALE','null')),   
    epaisseur INTEGER,
    surface FLOAT,   
    code_region INT,
    code_departement TEXT,
    cout_total_ht FLOAT,
    cout_induit_ht FLOAT,
    annee_travaux INTEGER,
    type_logement TEXT,
    annee_construction_logement INTEGER,
    CONSTRAINT fk_Isolation_region FOREIGN KEY (code_region) REFERENCES Regions(code_region),
    CONSTRAINT fk_Isolation_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement),
    CONSTRAINT fk_isolation_id_travaux FOREIGN KEY (id_travaux) REFERENCES Travaux(id_renovation)
);

CREATE TABLE IF NOT EXISTS Chauffages (
    id_travaux  PRIMARY KEY,
    energie_av_trav TXT CHECK(energie_av_trav IN ('AUTRES', 'BOIS', 'ELECTRICITE', 'FIOUL', 'GAZ','null')),
    energie_installee TXT CHECK(energie_installee IN ('AUTRES', 'BOIS', 'ELECTRICITE', 'FIOUL', 'GAZ',  'null')),
    generateur TXT check (generateur IN ('AUTRES', 'CHAUDIERE', 'INSERT', 'PAC', 'POELE', 'RADIATEUR','null')),
    type_chaud TXT CHECK(type_chaud IN ('STANDARD', 'AIR-EUA', 'A CONDENSATION', 'AUTRES', 'AIR-AIR', 'GEOTHERMIE', 'HPE','null')),
    code_region INT,
    code_departement TEXT,
    cout_total_ht FLOAT,
    cout_induit_ht FLOAT,
    annee_travaux INTEGER,
    type_logement TEXT,
    annee_construction_logement INTEGER,
    CONSTRAINT fk_Chauffage_region FOREIGN KEY (code_region) REFERENCES Regions(code_region),
    CONSTRAINT fk_Chauffage_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement),
    CONSTRAINT fk_chauffage_id_travaux FOREIGN KEY (id_travaux) REFERENCES Travaux(id_renovation)
);

CREATE TABLE IF NOT EXISTS Photovoltaiques (
    id_travaux  PRIMARY KEY,
    puissance_installee INTEGER,
    type_panneaux TEXT CHECK(type_panneaux IN ('MONOCRISTALLIN', 'POLYCRISTALLIN','null')),
    code_region INT,
    code_departement TEXT,
    cout_total_ht FLOAT,
    cout_induit_ht FLOAT,
    annee_travaux INTEGER,
    type_logement TEXT,
    annee_construction_logement INTEGER,
    CONSTRAINT fk_Photovoltaique_region FOREIGN KEY (code_region) REFERENCES Regions(code_region),
    CONSTRAINT fk_Photovoltaique_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement),
    CONSTRAINT fk_Photovoltaique_id_travaux FOREIGN KEY (id_travaux) REFERENCES Travaux(id_renovation)
);




