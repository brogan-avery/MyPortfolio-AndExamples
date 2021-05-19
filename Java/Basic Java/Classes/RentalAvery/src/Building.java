//Brogan Avery
public class Building {
private String buildingName;
private boolean hasPool;

//constructors
public Building() {
	super();
}

public Building(String buildingName, boolean hasPool) {
	super();
	this.buildingName = buildingName;
	this.hasPool = hasPool;
}
//getters
public String getBuildingName() {
	return buildingName;
}

public boolean isHasPool() {
	return hasPool;
}

public void setBuildingName(String buildingName) {
	this.buildingName = buildingName;
}

public void setHasPool(boolean hasPool) {
	this.hasPool = hasPool;
}

@Override
public String toString() {
	return "Building [buildingName=" + buildingName + ", hasPool=" + hasPool + "]";
}

}
