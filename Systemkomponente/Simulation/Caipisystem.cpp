/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Caipisystem
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Caipisystem.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Caipisystem.h"
//#[ ignore
#define System_Caipisystem_Caipisystem_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Caipisystem
Caipisystem::Caipisystem(IOxfActive* theActiveContext) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Caipisystem, Caipisystem(), 0, System_Caipisystem_Caipisystem_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        {
            itsKarussell.setShouldDelete(false);
        }
        {
            itsEinAusgabe.setShouldDelete(false);
        }
        {
            itsLimetten.setShouldDelete(false);
        }
        {
            itsZucker.setShouldDelete(false);
        }
        {
            itsCachacca.setShouldDelete(false);
        }
        {
            itsEis.setShouldDelete(false);
        }
        {
            itsStampfer.setShouldDelete(false);
        }
    }
    initRelations();
    //#[ operation Caipisystem()
    itsKarussell.addItsStation( &itsEinAusgabe);
    itsKarussell.addItsStation( &itsZucker);
    itsKarussell.addItsStation( &itsLimetten);
    itsKarussell.addItsStation( &itsStampfer);
    itsKarussell.addItsStation( &itsCachacca);
    itsKarussell.addItsStation( &itsEis);
    itsEinAusgabe.setStationsNr( 0 );
    itsZucker.setStationsNr( 1 );
    itsLimetten.setStationsNr( 2 );
    itsStampfer.setStationsNr( 3 );
    itsCachacca.setStationsNr( 4 );
    itsEis.setStationsNr( 5 );
                              
    //#]
}

Caipisystem::~Caipisystem() {
    NOTIFY_DESTRUCTOR(~Caipisystem, true);
}

Cachacca* Caipisystem::getItsCachacca() const {
    return (Cachacca*) &itsCachacca;
}

EinAusgabe* Caipisystem::getItsEinAusgabe() const {
    return (EinAusgabe*) &itsEinAusgabe;
}

Eis* Caipisystem::getItsEis() const {
    return (Eis*) &itsEis;
}

Karussell* Caipisystem::getItsKarussell() const {
    return (Karussell*) &itsKarussell;
}

int Caipisystem::getItsLed() const {
    int iter = 0;
    return iter;
}

Lichtschranke* Caipisystem::getItsLichtschranke() const {
    return (Lichtschranke*) &itsLichtschranke;
}

Limetten* Caipisystem::getItsLimetten() const {
    return (Limetten*) &itsLimetten;
}

Stampfer* Caipisystem::getItsStampfer() const {
    return (Stampfer*) &itsStampfer;
}

int Caipisystem::getItsWaage() const {
    int iter = 0;
    return iter;
}

Zucker* Caipisystem::getItsZucker() const {
    return (Zucker*) &itsZucker;
}

bool Caipisystem::startBehavior() {
    bool done = true;
    done &= itsCachacca.startBehavior();
    done &= itsEinAusgabe.startBehavior();
    done &= itsEis.startBehavior();
    done &= itsKarussell.startBehavior();
    done &= itsLimetten.startBehavior();
    done &= itsStampfer.startBehavior();
    done &= itsZucker.startBehavior();
    done &= OMReactive::startBehavior();
    return done;
}

void Caipisystem::initRelations() {
    {
        int toIter = 0;
        for (int i = 0; i < 6; i++) 
        {
            itsKarussell.addItsWaage(((Waage*)&itsWaage[toIter]));
            toIter++;
        }
        
    }
    {
        int toIter = 0;
        for (int i = 0; i < 6; i++) 
        {
            itsKarussell.addItsLed(((Led*)&itsLed[toIter]));
            toIter++;
        }
        
    }
    itsLichtschranke.setItsLimetten(&itsLimetten);
    itsLimetten.setItsLichtschranke(&itsLichtschranke);
}

void Caipisystem::setActiveContext(IOxfActive* theActiveContext, bool activeInstance) {
    OMReactive::setActiveContext(theActiveContext, activeInstance);
    {
        itsKarussell.setActiveContext(theActiveContext, false);
        itsEinAusgabe.setActiveContext(theActiveContext, false);
        itsLimetten.setActiveContext(theActiveContext, false);
        itsZucker.setActiveContext(theActiveContext, false);
        itsCachacca.setActiveContext(theActiveContext, false);
        itsEis.setActiveContext(theActiveContext, false);
        itsStampfer.setActiveContext(theActiveContext, false);
    }
}

void Caipisystem::destroy() {
    itsCachacca.destroy();
    itsEinAusgabe.destroy();
    itsEis.destroy();
    itsKarussell.destroy();
    itsLimetten.destroy();
    itsStampfer.destroy();
    itsZucker.destroy();
    OMReactive::destroy();
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedCaipisystem::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsKarussell", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsKarussell);
    aomsRelations->addRelation("itsWaage", true, false);
    {
        int iter = 0;
        while (iter < 6){
            aomsRelations->ADD_ITEM(((Waage*)&myReal->itsWaage[iter]));
            iter++;
        }
    }
    aomsRelations->addRelation("itsLed", true, false);
    {
        int iter = 0;
        while (iter < 6){
            aomsRelations->ADD_ITEM(((Led*)&myReal->itsLed[iter]));
            iter++;
        }
    }
    aomsRelations->addRelation("itsEinAusgabe", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsEinAusgabe);
    aomsRelations->addRelation("itsLimetten", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsLimetten);
    aomsRelations->addRelation("itsZucker", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsZucker);
    aomsRelations->addRelation("itsCachacca", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsCachacca);
    aomsRelations->addRelation("itsEis", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsEis);
    aomsRelations->addRelation("itsLichtschranke", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsLichtschranke);
    aomsRelations->addRelation("itsStampfer", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsStampfer);
}
//#]

IMPLEMENT_REACTIVE_META_SIMPLE_P(Caipisystem, System, System, false, OMAnimatedCaipisystem)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Caipisystem.cpp
*********************************************************************/
