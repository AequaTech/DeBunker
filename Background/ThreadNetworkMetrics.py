import sys
sys.path.append('../')
from sqlalchemy import create_engine,or_
from sqlalchemy.orm import sessionmaker
from API.database import Links,Base,Urls,DomainsWhois,DomainsNetworkMetrics
import datetime
import igraph as ig
import numpy as np


class ThreadNetworkMetrics:
    
    @staticmethod
    def retrieveDomains(self):

        SQLALCHEMY_DATABASE_URL = "sqlite:///../API/debunker.db"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)

        db = SessionLocal()
        link_objects = db.query(Links)
        G = ig.Graph(directed=True)
        links = []
        weights = []
        for link_object in link_objects:
            if link_object.weight > 0:
                links.append([link_object.source, link_object.target])
                weights.append(link_object.weight)
        G.add_vertices([v for s in links for v in s])
        G.add_edges(links)
        G.es['weight'] = weights

        print(weights)
        print(G.vcount())
        print(G.ecount())
        hub_score = G.hub_score(weights='weight')
        print(np.min(hub_score), np.max(hub_score))
        authority_score = G.authority_score(weights='weight')
        print(np.min(authority_score), np.max(authority_score))
        betweenness = G.betweenness(directed=True, weights='weight')
        print(np.min(betweenness), np.max(betweenness))
        betweenness_norm = (betweenness - np.min(betweenness)) / (np.max(betweenness) - np.min(betweenness))
        print(np.min(betweenness_norm), np.max(betweenness_norm))

        closeness = G.closeness(weights='weight', mode='out')
        print(np.min(closeness), np.max(closeness))
        closeness = np.nan_to_num(closeness)
        closeness_norm = (closeness - np.min(closeness)) / (np.max(closeness) - np.min(closeness))
        print(np.min(closeness_norm), np.max(closeness_norm))

        current_time = datetime.datetime.utcnow()
        ten_weeks_ago = current_time - datetime.timedelta(weeks=10)

        for node in G.vs:
            print(node)


                