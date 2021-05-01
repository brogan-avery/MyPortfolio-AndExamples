package mainPackage.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import mainPackage.beans.Location;

public interface LocationRepository extends JpaRepository<Location, Long>{ 

}
